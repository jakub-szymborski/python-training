MODULE injector_inputs
    
    INTEGER, PARAMETER          :: max_c        = 100                ! liczba komorek  ! bylo 80 
    INTEGER, PARAMETER          :: max          = 2*max_c + 2        ! liczba wezlow 
    DOUBLE PRECISION, PARAMETER :: dt_max       = 1.d-5      ! max. krok czasowy    
    DOUBLE PRECISION, PARAMETER :: eps_rel      = 6d-4            ! chropowatosc wzgledna, episilon / srednice, zakres: 10-6, 10-2
    DOUBLE PRECISION, PARAMETER :: pi           = 3.141592d0     
    
    DOUBLE PRECISION :: dt_inj_0, CFL 
    
    DOUBLE PRECISION :: channel_length, D1, D2, x1
    DOUBLE PRECISION :: angle
    INTEGER          :: n_channels
    
    DOUBLE PRECISION :: theta 
    DOUBLE PRECISION :: t_valve 
    DOUBLE PRECISION :: dp_limit 
    
    INTEGER :: skip 
    
    DOUBLE PRECISION :: cc, lambda, lambda_diff
    DOUBLE PRECISION :: p_test, u_test
    DOUBLE PRECISION :: dz
    
    CONTAINS 
    
    SUBROUTINE read_injector_inputs
        IMPLICIT NONE 
        !read inputs 
        
        CHARACTER(LEN = 50) :: path_injector 
        path_injector = "inputs\injector_inputs.txt"
    
        OPEN(UNIT=11, FILE=path_injector)    
        
        READ(11,*) dt_inj_0
        READ(11,*) t_valve
        READ(11,*) dp_limit 

        READ(11,*) CFL

        READ(11,*) channel_length
        dz     = channel_length/max_c

        READ(11,*) D1
        READ(11,*) D2
        
        READ(11,*) x1 
        READ(11,*) angle 
        READ(11,*) n_channels 
        
        READ(11,*) theta 
        
        READ(11,*) skip 
        
        READ(11,*) cc 
        READ(11,*) lambda
        READ(11,*) lambda_diff
        
        READ(11,*) p_test
        READ(11,*) u_test
    
        CLOSE(11)
        
    END SUBROUTINE read_injector_inputs 
    
    
    END MODULE injector_inputs