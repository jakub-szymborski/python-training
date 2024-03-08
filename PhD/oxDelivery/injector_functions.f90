MODULE injector_functions
    CONTAINS
   
    DOUBLE PRECISION FUNCTION friction_coefficient(Re_in) 
        ! funkcja liczaca wsp. oporu Darcy-Weisbacha, w zaleznosci od liczby reynoldsa 
        USE injector_inputs
        
        IMPLICIT NONE

        DOUBLE PRECISION,INTENT(IN) :: Re_in
        DOUBLE PRECISION :: f = 0.008

        if (Re_in > 0 .and. Re_in < 5000) then
            f = 64/Re_in

        elseif (Re_in > 0 .and. Re_in <= 1d8) then
            f = 0.25d0 / (log10( (eps_rel/3.7d0) + 5.74/Re_in**0.9d0))**2d0
    
        else 
           f = 0.008
        endif

        friction_coefficient = f
    END FUNCTION friction_coefficient


   DOUBLE PRECISION FUNCTION friction(fc, rho, V, D)
        IMPLICIT NONE 
        DOUBLE PRECISION, INTENT(IN) :: fc
        DOUBLE PRECISION, INTENT(IN) :: rho
        DOUBLE PRECISION, INTENT(IN) :: V
        DOUBLE PRECISION, INTENT(IN) :: D
       
        friction = fc * rho * abs(V) /(2*D)        

    END FUNCTION friction 

    
   SUBROUTINE ksztalt_kanalu(z, D_kanal, A_kanal)
        USE injector_inputs
        IMPLICIT NONE 
        DOUBLE PRECISION, DIMENSION(0:MAX+1), INTENT(INOUT) :: z
        DOUBLE PRECISION, DIMENSION(0:MAX+1), INTENT(INOUT) :: D_kanal
        DOUBLE PRECISION, DIMENSION(0:MAX+1), INTENT(INOUT) :: A_kanal

        INTEGER          ::  j
        DOUBLE PRECISION :: x2
        INTEGER          :: a1, a2  ! liczba komorek 1, 2 czesci 

        ! x1 - dlugosc prostego kawalka, x2 - x1 -> odcinek zmiany srednicy, x2 -> xmax odcinek prosty 

            DO j=0,MAX,1
            z(j)=(j-1)*dz/2.d0   ! podzial na komorki 
            END DO
 
            IF (angle == 0.0) THEN 
                x2 = channel_length - x1
            ELSE
       
                x2   = x1 + 0.5*(D2-D1)/tand(angle)        ! odc. na ktorym bedzie zmiana srednicy, 0.5 bo licze na srednicach a nie promieniach 
            END IF 
   
            a1   = FLOOR(max*x1/channel_length)         ! liczba komorek pierwszej czesci 
            a2   = FLOOR(max*x2/channel_length)         ! - ' -     '    drugiej czesci  
    
   
            DO j = 0, a1-1, 1
                D_kanal(j) = D1
            END DO    
   
            DO j= a1, a2-1, 1
                D_kanal(j) = D1 + 2*(j-a1)*(channel_length/max)*tand(angle) ! 

            END DO 
    
            DO j = a2, MAX, 1
                D_kanal(j) = D2
            end do  

        DO j=0, MAX, 1 
            A_kanal(j) = n_channels*(0.25d0*pi*D_kanal(j)**2)
        enddo

        D_kanal(0) = D_kanal(1)
        A_kanal(0) = A_kanal(1)

        D_kanal(Max) = D_kanal(Max-1)
        A_kanal(Max) = A_kanal(Max-1)

        D_kanal(Max+1) = D_kanal(Max)
        A_kanal(Max+1) = A_kanal(Max)

   END SUBROUTINE ksztalt_kanalu
    
    
   SUBROUTINE add_gravity(grav)
        USE injector_inputs
        IMPLICIT NONE
        DOUBLE PRECISION, DIMENSION (0:MAX+1), INTENT(INOUT) :: grav
        INTEGER :: j
        
        DO j=0,MAX,1
            grav(j)=0.d0           ! funkcja grawitacji od z 
        END DO
   
   END SUBROUTINE add_gravity 
   
   SUBROUTINE add_heat(q)
        USE injector_inputs
        IMPLICIT NONE
        DOUBLE PRECISION, DIMENSION (0:MAX+1), INTENT(INOUT) :: q
        INTEGER :: j

        DO j=0,MAX,1
            q(j)=0.d0           ! funkcja zrodla ciepla od z 
        END DO
   
   END SUBROUTINE add_heat 
   
   DOUBLE PRECISION FUNCTION sound_speed(p, u, x)
       USE properties
       IMPLICIT NONE 
       
       DOUBLE PRECISION, INTENT(IN) :: p
       DOUBLE PRECISION, INTENT(IN) :: u
       DOUBLE PRECISION, INTENT(IN) :: x
       
       DOUBLE PRECISION :: dro_dU_cpx
       DOUBLE PRECISION :: dro_dP_cux
       DOUBLE PRECISION :: rho
       
       
        dro_dU_cpx = dro_du_cpx_fa(p, u, x)   ! od p, u, x
        dro_dP_cux = dro_dp_cux_fa(p, u, x)   ! od p, u, x
        rho =  rho_pe_N2O_fa(p, u)
        sound_speed = sqrt((rho*rho - p * dro_dU_cpx)/(rho*rho*dro_dP_cux))       ! ro*ro - p * (.....)
                
   END FUNCTION sound_speed
   
    
    SUBROUTINE TRISOL( A,B,C,D,X ) 
        USE injector_inputs
        DOUBLE PRECISION, DIMENSION (0:MAX_C),INTENT(IN) :: A,B,C,D
        DOUBLE PRECISION, DIMENSION (1:MAX_C),INTENT(OUT) :: X

        INTEGER :: I,J,K
        DOUBLE PRECISION, DIMENSION(1:MAX_C) ::   Q,L,U   

           U(1)=B(1) 

           DO I = 2, MAX_C, 1
              L(I)=A(I)/U(I-1) 
              U(I)=B(I)-L(I)*C(I-1) 
           ENDDO

           Q(1)=D(1) 

           DO I = 2, MAX_C, 1
              Q(I)=D(I)-L(I)*Q(I-1) 
           ENDDO
   
           X(MAX_C)=Q(MAX_C)/U(MAX_C) 

           DO I = MAX_C-1, 1, -1
              X(I)=(Q(I)-C(I)*X(I+1))/U(I) 
           ENDDO
   
    END SUBROUTINE TRISOL    
    
    
    END MODULE injector_functions