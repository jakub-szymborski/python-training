!****************************************************************************
!   oxidizerDelivery, Jakub Szymborski 07.2023
!****************************************************************************
    PROGRAM oxDelivery

    USE tank_inputs
    USE Tank_PIM
    
  !  USE injector_basic         ! jednoczesnie moze byc uzywany tylko 1 niestacjonarny model wtrysku 
    USE injector_diffusion
  !  USE injector_eq
    
    USE wtrysk_steady
    USE properties
    USE injector_functions
    USE injector_inputs

    IMPLICIT NONE 
    ! do liczenia Tank_PIM:        
        ! t0, t_end, T_out,
        ! timeopen - czas otwarcia zaworu 
    
    ! Tank_PIM_main(dt, m_ox, m_out, vector)
    ! vector:       stan zbiornika:
        ! y(1) - alfa_g []     - udzial gornej czesci (obj.)
        ! y(2) - pr [Pa]       - cisnienie  
        ! y(3) - hg [J/kg]    - entalpia gornej czesci 
        ! y(4) - hd [J/kg]    - entalpia dolnej czesci 
        ! y(5) - T_wall [K]    - temperatura scianki
    
    
DOUBLE PRECISION                    :: t                = 0.d0
DOUBLE PRECISION                    :: t_end            = 0.1d0 !100* 1.d-7 !0.006d0      ! [s]   czas prowadzenia obliczen   
DOUBLE PRECISION                    :: dt_tank          = 1.d-6      ! [s]      krok czasowy zbiornika nie moze za bardzo sie roznic od kroku wtrysku, ~100 krotna roznica jeszcze okej
DOUBLE PRECISION                    :: m_ox_tank        = m_ox     ! [kg]
DOUBLE PRECISION, DIMENSION(1:5)    :: vector_tank 
DOUBLE PRECISION, DIMENSION(1:4)    :: vector_inj
DOUBLE PRECISION                    :: p_0, hg_0, hd_0, u_0, rho_0, rhog_0, rhod_0, alfa_0
DOUBLE PRECISION, DIMENSION(1:2)    :: m_out 
DOUBLE PRECISION                    :: Pb           = 22.d5 ! cisnienie na wylocie wtryskiwacza

DOUBLE PRECISION                    :: p_inj, dt_inj, m_ox_wtrysk, u_inj, x_inj, alfa_inj     ! zmienne wtrysku 
DOUBLE PRECISION                    :: m_ox_wtrysk_steady
DOUBLE PRECISION, DIMENSION(1:7,0:MAX)  :: stanKanalu   
DOUBLE PRECISION, DIMENSION(1:7,0:MAX_C)  :: stan_kanalu_steady   

DOUBLE PRECISION                    :: v_feed, rho_feed             ! parametry w linii zasilajacej 
INTEGER                             :: injector_steps               ! liczba krokow wtrysku na 1 krok zbiornika 
INTEGER                             :: save_inj_results                       ! licznik krokow, do porownania z 'pomin'

DOUBLE PRECISION                    :: delta_p, delta_x    ! spadek cisnienia na wtrysku, zmiana st. suchosci na wtrysku 
DOUBLE PRECISION                    :: p_outlet, h_outlet, rho_outlet, T_outlet             ! parametry wylotowe z wtrysku 
DOUBLE PRECISION                    :: m_out_dyer_comparison
DOUBLE PRECISION                    :: soundSpeed, ptest, plot_speed
DOUBLE PRECISION                    :: err

 OPEN(UNIT=1, FILE='wyniki_tank.txt')            ! zbiornik
 OPEN(UNIT=2, FILE='wyniki_wtrysk_basic.txt')    ! wtrysk - podstawowe 
 OPEN(UNIT=3, FILE='wyniki_wtrysk_full.txt')     ! wtrysk - pelne 
 OPEN(UNIT=7, FILE='kroki.txt')     ! kroki czasowe

 CALL read_injector_inputs
 
!plot_speed = plot_sound_speed(30.d5)   ! funkcja do stworzenia pliku z predkosciami dzwieku, dla danego cisnienia 
!call plot_derivatives 

 !CALL initial_values     ! subrutyna ustalajaca wartosci poczatkowe 
 CALL test_values
! CALL plot_steady_state
 
save_inj_results = 0
 
    DO WHILE (t <= t_end)
        
        IF (vector_tank(2) <= Pb) THEN 
            print *, 'Cisnienia wyrownane, koniec.'
            EXIT 
        END IF  
            
        !CALL Tank_PIM_main(dt_tank, m_ox_tank, m_out(1)/dt_tank, vector_tank)  ! obliczenia zbiornika 
        
        dt_inj = dt_inj_0  
        p_inj  = vector_tank(2) ! - normalne uzycie 
        
        IF ( vector_tank(1) <= alfa_graniczne) THEN    ! przypadek z oboma elementami
            u_inj  = vector_tank(4) - p_inj/rho_feed      ! energia wlasciwa na wlocie do wtryskiwacza
        ELSE         
            u_inj = vector_tank(3) - p_inj/rho_feed ! gdy nie ma juz dolnej czesci 
        END IF 
        
        injector_steps = 1
        m_out(2) = 0.d0       ! zerowanie strumienia ktory wyplynal miedzy krokami zbiornika 

        vector_inj(1)   = p_inj
        vector_inj(2)   = x_inj
        vector_inj(3)   = alfa_inj
       
        IF (0 == 1) THEN
            OPEN(UNIT=5, FILE='wyniki-wtrysk_steady.txt')   ! wyniki wtrysk stan ustalony 

            CALL wtrysk_steady_calc(vector_inj, 1.d0, outlet_pressure(t, p_inj, Pb), stan_kanalu_steady, m_ox_wtrysk_steady)
            DO j = 1, max_c,1 
                WRITE(5,'(f18.8, I18, E18.8, E18.8, f18.8, f18.8, E18.8)') t, j, stan_kanalu_steady(1,j)/1e5, stan_kanalu_steady(2,j)/1e3, stan_kanalu_steady(3,j), stan_kanalu_steady(4,j), stan_kanalu_steady(5,j) 
            END DO
            CLOSE(5)
        END IF 
            
        DO WHILE ( t + dt_tank >= t + dt_inj * injector_steps)      ! licz wtrysk tak dlugo, az kroki czasowe na wtrysku dogonia 1 krok zbiornika
            
            CALL time_adapt(p_inj, u_inj, x_inj, dt_inj_0, dt_inj)                                        ! (p, u, x, dt_in, dt_out)   
            WRITE(7,'(E18.6, E18.6, E18.6, E18.6)') t, dt_inj_0, dt_inj 

          !  CALL injector_basic_calc(dt_inj, vector_inj, outlet_pressure(t, p_inj, Pb), stanKanalu, m_ox_wtrysk)
            CALL injector_diffusion_calc(dt_inj, vector_inj, outlet_pressure(t, p_inj, Pb), stanKanalu, m_ox_wtrysk)
          !  CALL injector_eq_calc(dt_inj, vector_inj, outlet_pressure(t, p_inj, Pb), stanKanalu, m_ox_wtrysk)

            injector_steps = injector_steps + 1
            m_out(2) = m_out(2) + m_ox_wtrysk      ! sumaryczny wyplyw [kg]
        
        CALL save_basic_inj_results
       
        IF (save_inj_results == skip) THEN    
            DO j = 0, MAX-1, 1 
                soundSpeed = sound_speed(stanKanalu(1,j), stanKanalu(2,j), stanKanalu(3,j))
                err = (rho_pe_N2O_fa(stanKanalu(1,j), stanKanalu(2,j)) - stanKanalu(5,j))  / rho_pe_N2O_fa(stanKanalu(1,j), stanKanalu(2,j))
                
                ! stan kanalu: 1 - P, 2 - u, 3 - x, 4 - V, 5 - rho
                WRITE(3,'(f18.8, I18, E18.8, E18.8, f18.8, f18.8, E18.8, f18.8, f18.8, f18.8 )') t, j, stanKanalu(1,j), stanKanalu(2,j), stanKanalu(3,j), stanKanalu(4,j), stanKanalu(5,j), stanKanalu(7,j), abs(stanKanalu(4,j))/soundSpeed, err   
                save_inj_results = 0
            END DO
        END IF
        
        save_inj_results = save_inj_results + 1
        m_ox_tank = m_ox_tank - m_out(2)   ! aktualizacja masy w zbiorniku 
        m_out(1) = m_out(2)
        
        IF (m_ox_tank <= 0.d0) THEN
            PRINT *,'Zbiornik jest pusty.' 
            EXIT 
        END IF 
        
        m_out_dyer_comparison = m_out_dyer(t, T_ph_N2O_fa(vector_tank(2), vector_tank(4)), vector_tank(2), vector_tank(4))
        ! zbiornik: t,udzial gornej czesci, cisnienie, entalpia gornej czesci, entalpia dolnej czesci, temperatura scianki, mas. stopien suchosci dolnej czesci, masa utleniacza w zb.
        WRITE(1,'(f18.8, E22.6, E18.6, E18.6, E18.6, F18.2, E18.6, F12.6, F12.6)') t, vector_tank(1), vector_tank(2)/1e5, vector_tank(3)/1e3, vector_tank(4)/1e3, vector_tank(5), x_inj, m_ox_tank, m_out_dyer_comparison ! zapis do pliku zbiornik
        WRITE(*,'(f18.6, F12.4, E18.6, E18.6, E18.6)') t, vector_tank(1), vector_tank(2)/1e5, vector_tank(5), m_ox_tank     ! wyswietlanie w konsoli

         t = t + dt_tank
        END DO 
        END DO 

     CLOSE(1)
     CLOSE(2)
     CLOSE(3)
     CLOSE(7)

    CONTAINS 
  
    
 DOUBLE PRECISION FUNCTION m_out_dyer(time_dyer, Td, pd, hd)
! liczenie wyplywu z modelu SPI-HEM Dyera     
    USE tank_inputs
    USE injector_inputs
    USE paramfiz
    IMPLICIT NONE    

    DOUBLE PRECISION,INTENT(IN)     :: Td       ! temperatura cieczy
    DOUBLE PRECISION,INTENT(IN)     :: pd       ! cisnienie cieczy
    DOUBLE PRECISION,INTENT(IN)     :: hd       ! entalpia cieczy
    DOUBLE PRECISION,INTENT(IN)     :: time_dyer       ! aktualny czas 

    DOUBLE PRECISION :: Cp, Temp2, h2, rho2
    DOUBLE PRECISION :: m_ox_spi, m_ox_hem, kappa
    DOUBLE PRECISION :: rho
    DOUBLE PRECISION :: CdA
    DOUBLE PRECISION :: p_out_dyer

    CdA = 1.0* D1*D1* 3.141592d0*0.25*n_channels ! Cd = 0.5 * A wtrysku, do wstepnego okreslenia przeplywu
    
    rho = rho_ph_N2O_fa(pd, hd) 
    Cp = 27.67988 + 51.14898 * (Td / 1000) - 30.64454 * (Td / 1000)**2 + 6.847911 * (Td / 1000)**3 -0.157906/((Td/1000)**2); ! Cp w J/molK
    Cp = 1000*Cp/MN2O  ! przeliczenie z J/molK na J/kgK
    
    p_out_dyer = outlet_pressure(time_dyer, pd,Pb)
    
    Temp2 = Td / ((pd / p_out_dyer)**((kn2o-1.0)/kn2o));
    Temp2  = Td * (p_out_dyer/pd)**((kn2o-1.0)/kn2o) 
    
    !h2 = hd - Cp * Temp2;
    h2  = hd + Cp*(Temp2-Td)
    
    rho2 = rho_ph_N2O_fa(p_out_dyer,h2) 
    m_ox_SPI = CdA*sqrt(2*rho*(pd-p_out_dyer));
    m_ox_HEM = CdA*rho2*sqrt(2*(hd-h2));
    kappa = sqrt((pd - p_out_dyer) / (pd - p_out_dyer));

    m_out_dyer = (kappa * m_ox_SPI + m_ox_HEM) / (1 + kappa);
 END FUNCTION m_out_dyer
     

SUBROUTINE test_values
! do uzycia zamiast initialValues 
! subrutyna ustalajaca chciane parametry plynu na wlocie, do testow kanalu 
    IMPLICIT NONE 

    INTEGER :: j 
    p_0 = p_test ! zadane cisnienie 
    u_0 = u_test ! zadana en. wew.   
    
    IF ( 0 == 1)THEN    ! testy - impuls cisnienia
     IF (t == 0.d0) THEN 
       ptest = p_0
       DO j = 0, max, 1    ! stan poczatkowy kanalu 
           stanKanalu(1,j)     = ptest           ! x
       END DO 
        ELSE IF (t <= 0.002) THEN 
            ptest = p_0
        !ELSE IF ( t<=0.2) THEN
        !    ptest = 5.d0*t
        ELSE IF (t >0.002 .and. t <0.004) THEN 
            ptest = p_0 + 1e3
        ELSE
            ptest = p_0
        END IF
    END IF 
    
    rho_0 = m_ox_tank/Vol_in

    hg_0 = u_0 + p_0/rho_0      ! h = u + p/rho 
    hd_0 = u_0 + p_0/rho_0
    
    rhog_0 = rho_ph_N2O_fa(p_0,hg_0)           ! gêstoœæ w górnej czêsci zbiornika
    rhod_0 = rho_ph_N2O_fa(p_0,hd_0)           ! gêstoœæ w dolnej czêsci zbiornika
    
    IF (u_0 < esat_p_lqd(p_0)) THEN ! sama ciecz 
        rhog_0 = 0.d0
        rhod_0 = rho_0
        hg_0 = hd_0 
        alfa_0 = 0.d0 
    
        vector_tank(1)  = alfa_0      ! udzial obj. gornej czesci [m3/m3]
        vector_tank(2)  = p_0         ! cisnienie [Pa]
        vector_tank(3)  = hg_0        ! entalpia gornej czesci, [J/kg?]
        vector_tank(4)  = hd_0        ! entalpia dolnej czesci, [J/kg?]
        vector_tank(5)  = T_out       ! temperatura scianki zbiornika [K]
        rho_feed = rho_pe_N2O_fa(p_0, u_0)
    
        p_inj       = p_0
        u_inj       = u_0
        x_inj       = 0.d0
        alfa_inj    = 0.d0 
        
    ELSE IF (u_0 > esat_p_vap(p_0)) THEN ! sama para 
        rhod_0 = 0.d0
        alfa_0 = alfa_graniczne 
        CALL find_fluid_state
        hd_0   = hg_0 
    
        vector_tank(1)  = alfa_0      ! udzial obj. gornej czesci [m3/m3]
        vector_tank(2)  = p_0         ! cisnienie [Pa]
        vector_tank(3)  = hg_0        ! entalpia gornej czesci, [J/kg?]
        vector_tank(4)  = hd_0        ! entalpia dolnej czesci, [J/kg?]
        vector_tank(5)  = T_out       ! temperatura scianki zbiornika [K]
        rho_feed = rho_0
    
        p_inj       = p_0
        u_inj       = u_0
        x_inj       = Y_pealfa_N2O_fa(p_inj, u_inj, alfa_graniczne)                
        alfa_inj    = alfa_pY_N2O_fa(p_0,x_inj)
        
    ELSE    ! mieszanina 
        vector_tank(1)  = alfa_0      ! udzial obj. gornej czesci [m3/m3]
        vector_tank(2)  = p_0         ! cisnienie [Pa]
        vector_tank(3)  = hg_0        ! entalpia gornej czesci, [J/kg?]
        vector_tank(4)  = hd_0        ! entalpia dolnej czesci, [J/kg?]
        vector_tank(5)  = T_out       ! temperatura scianki zbiornika [K]
    
        p_inj       = p_0
        u_inj       = u_0
        rho_feed    = rho_pe_N2O_fa(p_0, u_0)
        x_inj       = Y_ph_N2O_fa(p_0,hd_0)
        alfa_inj    = alfa_pY_N2O_fa(p_0,x_inj) 
    END IF 
            
    ! czesc wspolna 
    m_out(1) =  m_out_dyer(dt_tank, T_0, p_0, hd_0) * dt_tank     ! poczatkowy strzal strumienia, do okreslenia predkosci w linii zasilajacej [kg]
    v_feed = 0.0010d0 !(m_out(1) / dt_tank) / (rho_feed * A_feed)         
        
    vector_inj(1)   = p_0                     ! cisnienie [Pa]      1- Pa, 2 - xa, 3 - alfaa, 4 - va
    vector_inj(2)   = x_inj                   ! stopien suchosci [kg/kg]  
    vector_inj(3)   = alfa_inj                ! stopien suchosci [m3/m3] 
    vector_inj(4)   = u_0                     ! 
    
    DO j = 0, max, 1    ! stan poczatkowy kanalu 
        stanKanalu(1,j)     = p_0             ! p
        stanKanalu(2,j)     = u_inj           ! u
        stanKanalu(3,j)     = x_inj           ! x
        stanKanalu(4,j)     = v_feed          ! w
        stanKanalu(5,j)     = rho_feed        ! rho
        stanKanalu(6,j)     = rho_feed*u_inj  ! rho U
        stanKanalu(7,j)     = x_inj           ! xr    
        WRITE(3,'(f18.8, I18, E18.8, E18.8, f18.8, f18.8, E18.8, f18.8, f18.8, f18.8 )') 0.d0, j, stanKanalu(1,j), stanKanalu(2,j), stanKanalu(3,j), stanKanalu(4,j), stanKanalu(5,j), stanKanalu(7,j), abs(stanKanalu(4,j))/soundSpeed, 0.d0
    END DO 
      
END SUBROUTINE test_values
 
 
SUBROUTINE initial_values
    ! procedura ustalajaca parametry poczatkowe w zaleznosci od temperatury poczatkowej
    IMPLICIT NONE 
   INTEGER :: j 
        p_0  = ps_T_N2O_fa(T_0) 
        hg_0 = hgs_p_N2O_fa(p_0) ! * 1.d0
        hd_0 = hls_p_N2O_fa(p_0) ! * 0.93d0 ! wartosc <1 skutkuje 'skokiem' cisnienia na poczatku przebiegu 

        rho_0 = m_ox_tank/Vol_in
        rhog_0 = rho_ph_N2O_fa(p_0,hg_0)           ! gêstoœæ w górnej czêsci zbiornika
        rhod_0 = rho_ph_N2O_fa(p_0,hd_0)           ! gêstoœæ w dolnej czêsci zbiornika
   
        alfa_0 = (rho_0 - rhod_0)/(rhog_0-rhod_0)
    
        !IF (rho_0 <= rhog_0) THEN   ! sama para 
        IF (alfa_0 >= alfa_graniczne) THEN
            rhod_0 = 0.d0
            alfa_0 = alfa_graniczne 
            
            CALL find_fluid_state
            
            hd_0   = hg_0 
    
            vector_tank(1)  = alfa_0      ! udzial obj. gornej czesci [m3/m3]
            vector_tank(2)  = p_0         ! cisnienie [Pa]
            vector_tank(3)  = hg_0        ! entalpia gornej czesci, [J/kg?]
            vector_tank(4)  = hd_0        ! entalpia dolnej czesci, [J/kg?]
            vector_tank(5)  = T_out       ! temperatura scianki zbiornika [K]
            rho_feed = rho_0
    
            p_inj       = p_0
            u_inj       = hd_0 - p_0/rho_0                  ! e = h - pv  => e = h - p/rho
            x_inj       = Y_pealfa_N2O_fa(p_inj, u_inj, alfa_graniczne)                
            alfa_inj    = alfa_pY_N2O_fa(p_0,x_inj)

        ELSE IF (rho_0 >= rhod_0) THEN ! sama ciecz 
            rhog_0 = 0.d0
            rhod_0 = rho_0
            hg_0 = hd_0 
            alfa_0 = 0.d0 
    
            vector_tank(1)  = alfa_0      ! udzial obj. gornej czesci [m3/m3]
            vector_tank(2)  = p_0         ! cisnienie [Pa]
            vector_tank(3)  = hg_0        ! entalpia gornej czesci, [J/kg?]
            vector_tank(4)  = hd_0        ! entalpia dolnej czesci, [J/kg?]
            vector_tank(5)  = T_out       ! temperatura scianki zbiornika [K]
            rho_feed = rho_0
    
            p_inj       = p_0
            u_inj       = hd_0 - p_0/rhod_0                  ! e = h - pv  => e = h - p/rho
            x_inj       = 0.d0
            alfa_inj    = 0.d0 
            
        ELSE ! mieszanina 
    
            vector_tank(1)  = alfa_0      ! udzial obj. gornej czesci [m3/m3]
            vector_tank(2)  = p_0         ! cisnienie [Pa]
            vector_tank(3)  = hg_0        ! entalpia gornej czesci, [J/kg?]
            vector_tank(4)  = hd_0        ! entalpia dolnej czesci, [J/kg?]
            vector_tank(5)  = T_out       ! temperatura scianki zbiornika [K]
            rho_feed = rho_ph_N2O_fa(p_0, hd_0)
    
            p_inj       = p_0
            u_inj       = hd_0 - p_0/rhod_0                  ! e = h - pv  => e = h - p/rho
            x_inj       = Y_ph_N2O_fa(p_0,hd_0)
            alfa_inj    = alfa_pY_N2O_fa(p_0,x_inj) 
            
        END IF 
           
        ! czesc wspolna 
        m_out(1) =  m_out_dyer(dt_tank, T_0, p_0, hd_0) * dt_tank     ! poczatkowy strzal strumienia, do okreslenia predkosci w linii zasilajacej [kg]
        v_feed = (m_out(1) / dt_tank) / (rho_feed * A_feed)        ! 
        
        vector_inj(1)   = p_0                     ! cisnienie [Pa]      1- Pa, 2 - xa, 3 - alfaa, 4 - va
        vector_inj(2)   = x_inj                   ! stopien suchosci [kg/kg]  
        vector_inj(3)   = alfa_inj                ! stopien suchosci [m3/m3]  
        vector_inj(4)   = u_inj
    
        DO j = 0, max, 1    ! stan poczatkowy kanalu 
            stanKanalu(1,j)     = p_0             ! p
            stanKanalu(2,j)     = u_inj           ! u
            stanKanalu(3,j)     = x_inj           ! x
            stanKanalu(4,j)     = v_feed          ! w
            stanKanalu(5,j)     = rho_feed        ! rho
            stanKanalu(6,j)     = rho_feed*u_inj  ! rho U
            stanKanalu(7,j)     = x_inj           ! xr    
          END DO 
END SUBROUTINE initial_values 
   

SUBROUTINE find_fluid_state
    ! procedura ustalajaca poczatkowy stan pary w zbiorniku jesli para jest przegrzana: rho = m/vol  <  rho(p_sat, h_sat) 
    ! z z rownania stanu:
    ! drho/dt = drho/dp * dp/dt + drho/dh * dh/dt,  /* dt
    ! drho   = drho/dp * dp + drho/dh * dh/dp * dp
    ! dp     = drho / (drho/dp + drho/dh * dh/dp)
    IMPLICIT NONE 
    DOUBLE PRECISION delta_ro, delta_pr, delta_h
    DOUBLE PRECISION p_temp, h_temp, delta_ro_temp 
    
    p_temp = p_0
    h_temp = hg_0
    delta_ro = rho_0 - rhog_0   ! roznica miedzy gestoscia rho = masa / vol a gestoscia rho(p_sat, h_sat) 
    
    DO WHILE (delta_ro < -0.1d0)
        delta_ro_temp = -0.1d0
        delta_pr = delta_ro_temp / (drhodp_ph_N2O_fa(p_0,hg_0) + drhodh_ph_N2O_fa(p_0,hg_0) * dhgsdp_p_N2O_fa(p_0))
        delta_h = delta_pr * dhgsdp_p_N2O_fa(p_0)
        p_0 = p_0 + delta_pr
        hg_0 = hg_0 + delta_h
        
        rhog_0 = rho_ph_N2O_fa(p_0,hg_0)
        delta_ro = rho_0 - rhog_0
        END DO 
    
END SUBROUTINE find_fluid_state


DOUBLE PRECISION FUNCTION outlet_pressure(time, p_lewo, p_prawo)
    !   Funkcja okreslajaca zmiennosc cisnienia zewnetrznego (Pb we wtrysku) od czasu 
    USE injector_inputs
    IMPLICIT NONE 
    
    DOUBLE PRECISION, INTENT(IN) :: time 
    DOUBLE PRECISION, INTENT(IN) :: p_lewo 
    DOUBLE PRECISION, INTENT(IN) :: p_prawo 
    
    IF (time < t_valve) THEN
        !outlet_pressure = 0.99*p_lewo + (p_prawo - p_lewo)*time/t_valve ! wersja A, cisnienie wylotowe malejace od P_tank do Pb 
        outlet_pressure = 0.9999*p_lewo - dp_limit * (time/t_valve)        ! wersja B, roznica cisnien rosnie liniowo do dp_limit      
    ELSE
        !outlet_pressure = p_prawo
        outlet_pressure = p_lewo - dp_limit
    END IF 
    
    
END FUNCTION outlet_pressure 
    

SUBROUTINE plot_sound_speed(givenPressure)
    IMPLICIT NONE

    DOUBLE PRECISION, INTENT(IN) :: givenPressure 
    DOUBLE PRECISION             :: energy, voidFrac, soundSpeed
    DOUBLE PRECISION             :: energyMin, energyMax, energyStep    
    DOUBLE PRECISION             :: density, drho_du_cpx, drho_dp_cux

    energyMin = 50d3
    energyMax = 450d3
    energy = energyMin 
    energyStep = (energyMax - energyMin)/1000

    OPEN(UNIT=6, FILE='soundSpeed.txt') ! predkosci dzwieku dla danego cisnienia 

    DO WHILE (energy <= energyMax)
    
        voidFrac = Y_pe_N2O_fa(givenPressure,energy)    ! (e - els) / (egs - els)

        soundSpeed = sound_speed(givenPressure, energy, voidFrac)
        energy  = energy + energyStep
        WRITE(6,'(f18.8, f18.8, f18.8, f18.8, f18.8, f18.8, f18.8)') givenPressure/10**5, energy/10**3, density, voidFrac, soundSpeed, drho_du_cpx, drho_dp_cux
    END DO 

    CLOSE(6) 
   
END SUBROUTINE plot_sound_speed
    

SUBROUTINE plot_derivatives
    IMPLICIT NONE 
    DOUBLE PRECISION :: dro_dP_cux, dro_dU_cpx, dro_dX_cpu
    DOUBLE PRECISION :: dro_dP_croux, dro_dROU_cpx, dro_dX_cprou
    DOUBLE PRECISION :: ptest, energy, voidFrac, density
    DOUBLE PRECISION :: el, vl, ugs, dvl_dul, vgs, dvolgs, dugs_dp, dul_dp_ux, dvol_lqd_dp
    DOUBLE PRECISION :: pmin, pmax, energyMin, energyMax
    DOUBLE PRECISION :: energyStep, pressureStep 
    INTEGER          :: steps = 1000
    
    pmin = 10e5
    pmax = 60e5
    pressureStep = (pmax - pmin)/steps
    
    energyMin = 50d3
    energyMax = 450d3
    energyStep = (energyMax - energyMin)/steps

    OPEN(UNIT=5, FILE='derivPlot.txt') !  

    ptest = pmin
    
        DO WHILE ( ptest <= pmax)
         energy = energyMin 
         DO WHILE (energy <= energyMax)
                density         =  rho_pe_N2O_fa(ptest, energy)
                voidFrac        =  Y_pe_N2O_fa(ptest, energy)
    
                dro_dP_cux      =  dro_dp_cux_fa(ptest, energy, voidFrac)
                dro_dU_cpx      =  dro_du_cpx_fa(ptest, energy, voidFrac)
                dro_dX_cpu      =  dro_dx_cpu_fa(ptest, energy, voidFrac)
    
               ! dro_dP_croux    =  density*dro_dP_cux / (density + energy * dro_dU_cpx)
               ! dro_dROU_cpx    =  dro_dU_cpx / (density + energy * dro_dU_cpx)
               ! dro_dX_cprou    =  density* dro_dX_cpu / (density + energy * dro_dU_cpx)
                
                ! do dro_dX
                el      = eliq_pex_N2O_fa(ptest,energy,voidFrac)
                vl      = 1/rhol_pe_N2O_fa(ptest,el)
                ugs     = esat_p_vap(ptest)
                dvl_dul = dvol_lqd_de_pe_N2O_fa(ptest,el) 
                vgs     = 1 / rhogs_p_N2O_fa(ptest)      ! obj. wlasciwa pary, z lini nasycenia 
                
                ! do dro_dP
                dvolgs      = dvolgs_p_fa(ptest) 
                dugs_dp     = dugs_p(ptest)                
                dul_dp_ux   = -(voidFrac/(1.d0-voidFrac)) * dugs_dp
                dvol_lqd_dp = dvol_lqd_dp_pe_N2O_fa(ptest, el)                   
            
                WRITE(5,'(f18.8, F18.8, F18.8, E18.8, E18.8, E18.8, F18.8, F18.8, E18.8, E18.8, E18.8, E18.8, E18.8, E18.8, E18.8, E18.8)') ptest/10**5, energy/10**3, density, voidFrac, dro_dP_cux, dro_dU_cpx, dro_dX_cpu, el, vl, ugs, dvl_dul, vgs, dvolgs, dugs_dp, dul_dp_ux, dvol_lqd_dp
                energy = energy + energyStep
         END DO 
         ptest = ptest + pressureStep 
        END DO 
        CLOSE(5) 

END SUBROUTINE plot_derivatives


SUBROUTINE time_adapt(p, u, x, dt_in, dt_out)

IMPLICIT NONE 
! funkcja adaptujaca krok czasowy do parametrow przeplywu
! nowy krok moze byc wielokrotnoscia wejsciowego
! parametry: CFL, dt0, dtmax, dz
DOUBLE PRECISION, INTENT(IN)    :: p,u,x, dt_in ! cisnienie [Pa], energia wew. [J/kg], krok wejsciowy [s], krok wyjsciowy [s] 
DOUBLE PRECISION, INTENT(OUT)   :: dt_out
DOUBLE PRECISION                :: a_sound
DOUBLE PRECISION :: dt_nowy
INTEGER          :: ndt

    a_sound = sound_speed(p,u,x) 
    dt_nowy = CFL * dz/a_sound
    
    IF ( dt_nowy > dt_in) THEN
        
        IF (dt_nowy >= dt_max) THEN   ! jesli krok jest wiekszy niz maksymalny, ograniczam do max
            dt_nowy = dt_max
        ELSE 
            ndt = int(dt_nowy/dt_in)  ! ile razy nowy krok miesci sie w starym 
            dt_nowy = ndt*dt_in            ! nowy krok ustawiony jako wielokrotnosc bazowego
        END IF 
    ELSE                            ! jesli nowy krok jest mniejszy/rowny niz bazowy, zostaje bazowy
        dt_nowy = dt_in
    END IF 

    dt_out = dt_nowy
    v=dz/dt_out         !  aktualizacja predkosc na siatce od kroku czasowego
    
    
END SUBROUTINE time_adapt


SUBROUTINE plot_steady_state
        USE injector_inputs
        USE properties
        USE wtrysk_steady

        IMPLICIT NONE 
        DOUBLE PRECISION             :: pressure, pressureMin, pressureMax, pressureStep 
        DOUBLE PRECISION             :: energy, p_avg, e_avg, rho_avg, v_avg, x_avg, strumien_avg
        DOUBLE PRECISION             :: energyMin, energyMax, energyStep    
        DOUBLE PRECISION,DIMENSION(1:4) :: vector_in   
        DOUBLE PRECISION             :: strumien_steady 
        DOUBLE PRECISION             :: V_guess, p_out 

        DOUBLE PRECISION, DIMENSION(1:7,0:MAX_C)  :: stan    
        INTEGER :: j
        
        OPEN(UNIT=5, FILE='mapa_wtrysk_steady.txt')   ! wyniki wtrysk stan ustalony 
    
        pressureMin = 20.d5
        pressureMax = 50.d5
        energyMin = 50.d3
        energyMax = 450.d3
    
        energy = energyMin 
        energyStep = (energyMax - energyMin)/40    
    
        pressure = pressureMin
        pressureStep = (pressureMax - pressureMin)/40
    
        ! petla po wszystkich cisnieniach
        DO WHILE (pressure < pressureMax)
            energy = energyMin
            p_out = pressure - dp_limit

            DO WHILE (energy < energyMax)
                p_avg = 0.d0
                e_avg = 0.d0
                x_avg = 0.d0
                v_avg = 0.d0
                rho_avg = 0.d0
                strumien_avg = 0.d0
        
                vector_in(1) = pressure
                vector_in(2) = 0.d0         ! x, nieuzywane w stacjonarnym
                vector_in(3) = 0.d0         ! alfa, nieuzywane w stacjonarnym
                vector_in(4) = energy
            
                V_guess = SQRT(2*(pressure-p_out)/rho_pe_N2O_fa(pressure, energy))
        
                CALL wtrysk_steady_calc(vector_in, V_guess, p_out, stan, strumien_steady)
                    DO j = 1, max_c,1     ! stan kanalu: 1 - P, 2 - u, 3 - x, 4 - V, 5 - rho
                        p_avg = p_avg + stan(1,j)
                        e_avg = e_avg + stan(2,j)
                        x_avg = x_avg + stan(3,j)
                        v_avg = v_avg + stan(4,j)
                        rho_avg = rho_avg + stan(5,j)
                    END DO
            
                p_avg   = p_avg / max_c
                e_avg   = e_avg / max_c
                x_avg   = x_avg / max_c
                v_avg   = v_avg / max_c
                rho_avg = rho_avg / max_c
                strumien_avg = strumien_steady

                WRITE(5,'(f18.8, E18.8, E18.8, f18.8, f18.8, E18.8, E18.8, E18.8, E18.8)') pressure/1e5, energy/1e3, p_avg/1e5, e_avg/1e3, x_avg, v_avg, rho_avg, strumien_avg
           
               WRITE(*,'(f18.8, f18.8, f18.8, f18.8)') pressure, p_out, energy, strumien_steady
               !WRITE(5,'(f18.8, f18.8, f18.8, f18.8, f18.8, f18.8, f18.8, f18.8, f18.8)') pressure, p_out, energy, V_guess, rho_pe_N2O_fa(pressure, energy), vector_in(1), vector_in(4) 
               energy = energy + energyStep
            END DO
        
            pressure = pressure + pressureStep

        END DO 
        CLOSE(5)
    
END SUBROUTINE plot_steady_state


SUBROUTINE save_basic_inj_results
	IMPLICIT NONE 
	DOUBLE PRECISION :: delta_p, delta_x    ! spadek cisnienia na wtrysku, zmiana st. suchosci na wtrysku 
	DOUBLE PRECISION :: p_outlet, h_outlet, rho_outlet, T_outlet             ! parametry wylotowe z wtrysku 
	
	delta_p  = stanKanalu(1,1) - stanKanalu(1,MAX) 
	delta_x  = stanKanalu(3,1) - stanKanalu(3,MAX) 
	p_outlet = stanKanalu(1,MAX)
	rho_outlet = stanKanalu(5,MAX)
	h_outlet = stanKanalu(2,MAX) + p_outlet/rho_outlet          ! e = h - pv  => e = h - p/rho       => h = e + p/rho
	T_outlet = T_ph_N2O_fa(p_outlet, h_outlet)
	
	WRITE(2,'(f18.8, E18.4, E18.4, E18.4, E18.4, E18.4, E18.4)') t, dt_inj, delta_p/1e5, delta_x, m_ox_wtrysk, T_outlet, rho_outlet ! zapis tylko raz na 1 krok zbiornika 

	END SUBROUTINE save_basic_inj_results




    END PROGRAM oxDelivery

    
    
