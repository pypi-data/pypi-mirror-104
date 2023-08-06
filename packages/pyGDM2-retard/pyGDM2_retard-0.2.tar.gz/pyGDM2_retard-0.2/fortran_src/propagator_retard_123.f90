!--------------------------------------------------!
!     dipoleSlab.f                                 !
!     Excitation Slab par dipole                   !
!==================================================!
! Gerard COLAS des FRANCS                          !
! 11 janvier 2000                                  ! 
! derniere modification : juin 2010                !
!--------------------------------------------------!
!==============================!
!     SUBROUTINES              !                   
!==============================!
!=====================================================!
!        propagateurs S(i,j)                          !
! ATTENTION unites c.g.s                              !
!=====================================================!
!--------------------------------------------------------------------!
! propagateur du vide                                                !
!--------------------------------------------------------------------!
	SUBROUTINE PROPAG0(eps,ak0,xd,yd,zd,s0)
	implicit none
	double precision::eps,ak0,xd,yd,zd
	double complex, intent(out) ::s0(9)
	double complex ::cim,coeff
	double precision::r,r5,r4,r3,r2,T3(9),T2(9),T1(9),k3,k32
	integer::l
!----------------------------!
! definitions preliminaires  !
!----------------------------!
	cim=dcmplx(0.d0,1.d0)
	k3=dsqrt(eps)*ak0
	r=dsqrt(xd*xd+yd*yd+zd*zd)
	r5=r**5
	r4=r**4
	r3=r**3
	r2=r**2
!----------------------!
! partie champ proche  !
!----------------------!
! 1ere ligne
	T3(1)=(3.d0*xd*xd-r2)/r5
	T3(2)=(3.d0*xd*yd)/r5
	T3(3)=(3.d0*xd*zd)/r5
! 2eme ligne
	T3(4)=T3(2)
	T3(5)=(3.d0*yd*yd-r2)/r5
	T3(6)=(3.d0*yd*zd)/r5
! 3eme ligne
	T3(7)=T3(3)
	T3(8)=T3(6)
	T3(9)=(3.d0*zd*zd-r2)/r5
!----------------------------!
! partie champ intermediaire !
!----------------------------!
! 1ere ligne
	T2(1)=(3.d0*xd*xd-r2)/r4
	T2(2)=(3.d0*xd*yd)/r4
	T2(3)=(3.d0*xd*zd)/r4
! 2eme ligne
	T2(4)=T2(2)
	T2(5)=(3.d0*yd*yd-r2)/r4
	T2(6)=(3.d0*yd*zd)/r4
! 3eme ligne
	T2(7)=T2(3)
	T2(8)=T2(6)
	T2(9)=(3.d0*zd*zd-r2)/r4
!------------------------!
! partie champ lointain  !
!------------------------!
! 1ere ligne
	T1(1)=(xd*xd-r2)/r3
	T1(2)=(xd*yd)/r3
	T1(3)=(xd*zd)/r3
! 2eme ligne
	T1(4)=T1(2)
	T1(5)=(yd*yd-r2)/r3
	T1(6)=(yd*zd)/r3
! 3eme ligne
	T1(7)=T1(3)
	T1(8)=T1(6)
	T1(9)=(zd*zd-r2)/r3
! formation des termes finaux
	k32=k3*k3
	coeff=cdexp(cim*k3*r)/eps
	do l=1,9
	   s0(l)=coeff*(-k32*T1(l)-cim*k3*T2(l)+T3(l))
	enddo
	RETURN     
	END
!!-------------------------------------------------------------------!
! propagateur de surface retarde S11                                 !
!--------------------------------------------------------------------!
	SUBROUTINE PROPAG11(eps1,eps2,eps3,d,ak0,a,xd,yd,z,z0,s11,q11)
	implicit none
	double precision::prec=1.d-6
	double precision::eps1,eps3,d,ak0,a,xd,yd,z,z0
	double complex  ::eps2
	double complex, intent(out) ::s11(9),q11(9)
	double precision ::pi,r,phi,trp(2),ki(3),kmax,kmaj,kmin&
     &	 ,k,t,dt,dk,n3,k3,wg(4),kinfinity&
     &   ,xgk(8),wgk(8),resabs(9),t0,t1,centr,hlgth,dhlgth,absc&
     &	 ,k0,k1,err0,abserr0
	double complex ::cim,c0,ck,dck,fc(9),resg(9),resk(9)&
     &	 ,fval1(9),fval2(9),fv1(7,9),fv2(7,9),fsum(9),gsum(9)&
     &   ,gc(9),bresg(9),bresk(9),gval1(9),gval2(9),gv1(7,9),gv2(7,9)

	integer ::l,nt,j,jtw,jtwm1

!----------------------------!
! definitions preliminaires  !
!----------------------------!
	c0=dcmplx(0.d0,0.d0)
	cim=dcmplx(0.d0,1.d0)
	pi=4.d0*datan(1.d0)
	
	
!	write(*,*) a, eps1,eps2,eps3
!	write(*,*) ak0,a
!	write(*,*) xd,yd,z,z0
	
	
! coordonnees cylindriques
	r=dsqrt(xd*xd+yd*yd)
	if (r .lt. a/2.d0) then
	   r=0.d0
	   phi=0.d0
	elseif (dabs(xd) .lt. a/2.d0) then
	   if (yd .ge. 0.d0) then 
	      phi=pi/2.d0
	   else 
	      phi=-pi/2.d0
	   endif
	elseif (dabs(yd) .lt. a/2.d0) then
	   if (xd .ge. 0.d0) then 
	      phi=0.d0
	   else 
	      phi=-pi
	   endif
	else
	   if (xd .ge. 0.d0) then 
	      phi=datan(yd/xd)
	   elseif (xd .le. 0.d0) then
	      phi=datan(yd/xd)+pi
	   else
	      write(*,*)'probleme ds definition coord. cyl. !'
	   endif 
	endif
! 	print *, "A", r, phi
	trp(1)=dcos(phi)
	trp(2)=dsin(phi)
! initialisation propagateur
	do l=1,9
	   s11(l)=c0
	   q11(l)=c0
	enddo
! definition du chemin d'integration
! integration le long de k_parrallele
! contournement des singularites
	ki(1)=dsqrt(eps1)*ak0
	ki(2)=dble(cdsqrt(eps2)*ak0)
	ki(3)=dsqrt(eps3)*ak0
	kmax=0.d0
	do l=1,3
	   if (ki(l) .gt. kmax) then 
	      kmax=ki(l)
	   endif
	enddo
	kmaj=(ak0+kmax)/2.d0
	kmin=0.001d0*kmaj
!==============================================
! Algorithme de Gauss Kronrod
! coefficients 
	WG(1)=0.129484966168869693270611432679082d0
	WG(2)=0.279705391489276667901467771423780d0
	WG(3)=0.381830050505118944950369775488975d0
	WG(4)=0.417959183673469387755102040816327d0
!
	XGK(1)=0.991455371120812639206854697526329d0
	XGK(2)=0.949107912342758524526189684047851d0
	XGK(3)=0.864864423359769072789712788640926d0
	XGK(4)=0.741531185599394439863864773280788d0
	XGK(5)=0.586087235467691130294144838258730d0
	XGK(6)=0.405845151377397166906606412076961d0
	XGK(7)=0.207784955007898467600689403773245d0
	XGK(8)=0.000000000000000000000000000000000d0
!
	WGK(1)=0.022935322010529224963732008058970d0
	WGK(2)=0.063092092629978553290700663189204d0
	WGK(3)=0.104790010322250183839876322541518d0
	WGK(4)=0.140653259715525918745189590510238d0
	WGK(5)=0.169004726639267902826583426598550d0
	WGK(6)=0.190350578064785409913256402421014d0
	WGK(7)=0.204432940075298892414161999234649d0
	WGK(8)=0.209482141084727828012999174891714d0
!
!***FIRST EXECUTABLE STATEMENT  DQK15
!
! integration dans le plan complexe (t entre 0 et pi)
	nt=0
	t0=0.d0
	t1=pi
 25	nt=nt+1
        centr = 0.5d+00*(t0+t1)
	hlgth = 0.5d+00*(t1-t0)
	dhlgth = dabs(hlgth)
!
!           compute the 15-point kronrod approximation to
!           the integral, and estimate the absolute error.
!
        ck=dcmplx(kmaj-kmaj*dcos(centr),-kmin*dsin(centr))
	dck=dcmplx(kmaj*dsin(centr),-kmin*dcos(centr))
        call FC11(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,fc,gc)
	do l=1,9
	   resg(l) = fc(l)*wg(4)
	   resk(l) = fc(l)*wgk(8)
!
	   bresg(l) = gc(l)*wg(4)
	   bresk(l) = gc(l)*wgk(8)
	enddo
	do 10 j=1,3
	   jtw = j*2
	   absc = hlgth*xgk(jtw)
	   t=centr-absc
	   ck=dcmplx(kmaj-kmaj*dcos(t),-kmin*dsin(t))
	   dck=dcmplx(kmaj*dsin(t),-kmin*dcos(t))
	call FC11(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,fval1,gval1)
	   t=centr+absc
	   ck=dcmplx(kmaj-kmaj*dcos(t),-kmin*dsin(t))
	   dck=dcmplx(kmaj*dsin(t),-kmin*dcos(t))
        call FC11(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,fval2,gval2)
        do l=1,9
           fv1(jtw,l) = fval1(l)
           fv2(jtw,l) = fval2(l)
           fsum(l) = fval1(l)+fval2(l)
           resg(l) = resg(l)+wg(j)*fsum(l)
           resk(l) = resk(l)+wgk(jtw)*fsum(l)
!
           gv1(jtw,l) = gval1(l)
           gv2(jtw,l) = gval2(l)
           gsum(l) = gval1(l)+gval2(l)
           bresg(l) = bresg(l)+wg(j)*gsum(l)
           bresk(l) = bresk(l)+wgk(jtw)*gsum(l)
        enddo
 10	CONTINUE
	DO 15 j = 1,4
	   jtwm1 = j*2-1
	   absc = hlgth*xgk(jtwm1)
	   t=centr-absc
	   ck=dcmplx(kmaj-kmaj*dcos(t),-kmin*dsin(t))
	   dck=dcmplx(kmaj*dsin(t),-kmin*dcos(t))
	call FC11(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,fval1,gval1)
        t=centr+absc
        ck=dcmplx(kmaj-kmaj*dcos(t),-kmin*dsin(t))
        dck=dcmplx(kmaj*dsin(t),-kmin*dcos(t))
	call FC11(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,fval2,gval2)
        do l=1,9
           fv1(jtwm1,l) = fval1(l)
           fv2(jtwm1,l) = fval2(l)
           fsum(l) = fval1(l)+fval2(l)
           resk(l) = resk(l)+wgk(jtwm1)*fsum(l)
!
           gv1(jtwm1,l) = gval1(l)
           gv2(jtwm1,l) = gval2(l)
           gsum(l) = gval1(l)+gval2(l)
           bresk(l) = bresk(l)+wgk(jtwm1)*gsum(l)
        enddo
 15	CONTINUE
	abserr0=0.d0
	err0=0.d0
	do l=1,9
	   abserr0=abserr0+cdabs((resk(l)-resg(l)))*hlgth
           err0=err0+cdabs(s11(l)+resk(l)*hlgth)
	enddo
        abserr0=abserr0/err0
	if ((abserr0) .le. prec) then 
	   do l=1,9
	      s11(l)=s11(l)+resk(l)*hlgth
	      q11(l)=q11(l)+bresk(l)*hlgth
	   enddo
	   if (t1 .lt. pi) then
	      t0=t1
	      t1=pi
	      goto 25 
	   endif
	else
	   t1=centr
	   goto 25
	endif
! poursuite de l'integration le long axe reel
	nt=0
	kinfinity=500.d0*kmaj
	k0=0.d0
	k1=kinfinity
 300	nt=nt+1
        centr = 0.5d+00*(k0+k1)
	hlgth = 0.5d+00*(k1-k0)
	dhlgth = dabs(hlgth)
!
!           compute the 15-point kronrod approximation to
!           the integral, and estimate the absolute error.
!
      call FR11(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,2.d0*kmaj,centr,fc,gc)
      do l=1,9
         resg(l) = fc(l)*wg(4)
         resk(l) = fc(l)*wgk(8)
!
         bresg(l) = gc(l)*wg(4)
         bresk(l) = gc(l)*wgk(8)
      enddo
      do 100 j=1,3
        jtw = j*2
        absc = hlgth*xgk(jtw)
	k=centr-absc
      call FR11(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,2.d0*kmaj,k,&
     &       fval1,gval1)
	k=centr+absc
      call FR11(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,2.d0*kmaj,k,&
     &       fval2,gval2)
      do l=1,9
         fv1(jtw,l) = fval1(l)
         fv2(jtw,l) = fval2(l)
         fsum(l) = fval1(l)+fval2(l)
         resg(l) = resg(l)+wg(j)*fsum(l)
         resk(l) = resk(l)+wgk(jtw)*fsum(l)
!
         gv1(jtw,l) = gval1(l)
         gv2(jtw,l) = gval2(l)
         gsum(l) = gval1(l)+gval2(l)
         bresg(l) = bresg(l)+wg(j)*gsum(l)
         bresk(l) = bresk(l)+wgk(jtw)*gsum(l)
      enddo
 100  CONTINUE
      DO 150 j = 1,4
	jtwm1 = j*2-1
	absc = hlgth*xgk(jtwm1)
	k=centr-absc
      call FR11(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,2.d0*kmaj,k,&
     &       fval1,gval1)
      k=centr+absc
      call FR11(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,2.d0*kmaj,k,&
     &     fval2,gval2)
      do l=1,9
         fv1(jtwm1,l) = fval1(l)
         fv2(jtwm1,l) = fval2(l)
         fsum(l) = fval1(l)+fval2(l)
         resk(l) = resk(l)+wgk(jtwm1)*fsum(l)
!
         gv1(jtwm1,l) = gval1(l)
         gv2(jtwm1,l) = gval2(l)
         gsum(l) = gval1(l)+gval2(l)
         bresk(l) = bresk(l)+wgk(jtwm1)*gsum(l)
      enddo
 150  CONTINUE
      abserr0=0.d0
      err0=0.d0
      do l=1,9
         abserr0=abserr0+cdabs((resk(l)-resg(l)))*hlgth
         err0=err0+cdabs(s11(l)+resk(l)*hlgth)
      enddo
      abserr0=abserr0/err0
      if ((abserr0) .le. prec) then 
         do l=1,9
            s11(l)=s11(l)+resk(l)*hlgth
            q11(l)=q11(l)+bresk(l)*hlgth
         enddo
         if (k1 .lt. kinfinity) then
            k0=k1
            k1=kinfinity
            goto 300 
         endif
      else
         k1=centr
         goto 300 
      endif
! proprietes de symetrie
      s11(4)=s11(2)
      q11(5)=-q11(1)
!      g,*) s11(5)
      RETURN     
      END
!======================================================!
!================================================================
      SUBROUTINE FC11(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,&
     &     f11c,g11c)
      implicit none
      double precision::eps1,eps3,d,ak0,a,r,trp(2),z,z0
      double complex  ::eps2,ck,dck
      double complex ::f11c(9),g11c(9)
      double precision ::pi,k11,cop,sip,co2p,CYR(2),CYI(2)
      double complex   ::cim,c0,r12s,r12p,r23s,r23p,fs(9),fp(9), &
     &	 gs(9),gp(9),cj0,cj1,cj10,coeff,ww1,ww2,ww3,w1,w2,w3,rs,rp
      integer                    ::l,NZ,IERR
!----------------------------!
! definitions preliminaires  !
!----------------------------!
	c0=dcmplx(0.d0,0d0)
	cim=dcmplx(0.d0,1.d0)
	pi=4.d0*datan(1.d0)
	k11=eps1*ak0*ak0
	cop=trp(1)
	sip=trp(2)
	co2p=cop*cop-sip*sip
! initialisation
	do l=1,9
	   fs(l)=c0
	   fp(l)=c0
           gs(l)=c0
	   gp(l)=c0
	enddo
! fonctions de Bessel
	if (r .lt. 0.001d0) then
	   cj0=dcmplx(1.d0,0.d0)
	   cj1=c0
	   cj10=dcmplx(0.5d0,0.d0)
	else
        call ZBESJ(dble(ck*r),dimag(ck*r),0,1,2,CYR,CYI,NZ,IERR)
        cj0=dcmplx(CYR(1),CYI(1))
        cj1=dcmplx(CYR(2),CYI(2))
        cj10=cj1/(ck*r)
	endif
! vecteurs d'ondes dans chaque region
	ww1=eps1*ak0*ak0-ck*ck
	ww2=eps2*ak0*ak0-ck*ck
	ww3=eps3*ak0*ak0-ck*ck
	w1=cdsqrt(ww1)
	w2=cdsqrt(ww2)
	w3=cdsqrt(ww3)
	if (dimag(w1) .lt. 0.d0) then
	   w1=-w1
	endif
	if (dimag(w2) .lt. 0.d0) then
	   w2=-w2
	endif
	if (dimag(w3) .lt. 0.d0) then
	   w3=-w3
	endif
! coeff de Fresnel
! reflexion aux interfaces
	r12s=(w1-w2)/(w1+w2)
	r23s=(w2-w3)/(w2+w3)
	r12p=(eps2*w1-eps1*w2)/(eps2*w1+eps1*w2)
	r23p=(eps3*w2-eps2*w3)/(eps3*w2+eps2*w3)
! bilan reflexion 
	rs=(r12s+r23s*cdexp(2.d0*cim*w2*d))/&
     &       (1.d0+r12s*r23s*cdexp(2.d0*cim*w2*d))
	rp=(r12p+r23p*cdexp(2.d0*cim*w2*d))/&
     &       (1.d0+r12p*r23p*cdexp(2.d0*cim*w2*d))
!coeff des ondes planes
        coeff=cdexp(cim*w1*(z+z0))
! propagateur electrique
!1ere ligne
	fs(1)=k11*ck*rs*(sip*sip*cj0+co2p*cj10)/w1
	fp(1)=-w1*ck*rp*(cop*cop*cj0-co2p*cj10)
	fs(2)=-k11*ck*rs*sip*cop*(cj0-2.d0*cj10)/w1
	fp(2)=-w1*ck*rp*sip*cop*(cj0-2.d0*cj10)
	fp(3)=-cim*ck*ck*rp*cop*cj1
!2eme ligne
	fs(5)=k11*ck*rs*(cop*cop*cj0-co2p*cj10)/w1
	fp(5)=-w1*ck*rp*(sip*sip*cj0+co2p*cj10)
	fp(6)=-cim*ck*ck*rp*sip*cj1
! 3eme ligne
	fp(7)=cim*ck*ck*cop*rp*cj1
	fp(8)=cim*ck*ck*sip*rp*cj1
	fp(9)=ck*ck*ck*rp*cj0/w1
! propagateur mixte
!1ere ligne
	gs(1)=ck*rs*sip*cop*(cj0-2.d0*cj10)
	gp(1)=ck*rp*sip*cop*(cj0-2.d0*cj10)
	gs(2)=ck*rs*(cop*cop*cj0-co2p*cj10)
	gp(2)=ck*rp*(sip*sip*cj0+co2p*cj10)
	gp(3)=cim*rp*ck*ck*sip*cj1/w1
!2eme ligne
	gs(4)=ck*rs*(sip*sip*cj0+co2p*cj10)
	gp(4)=-ck*rp*(cop*cop*cj0-co2p*cj10)
	gp(6)=-cim*rp*ck*ck*cop*cj1/w1
! 3eme ligne
	gs(7)=-cim*rs*ck*ck*sip*cj1/w1
	gs(8)=cim*rs*ck*ck*cop*cj1/w1
! reconstruction
	do l=1,9
	   f11c(l)=(fs(l)+fp(l))*coeff*cim*dck/eps1
	   g11c(l)=(gs(l)+gp(l))*coeff*cim*dck
	enddo
	RETURN
	END
!==========================================================
      SUBROUTINE FR11(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,k0,k,f11r,g11r)
      implicit none
      double precision::eps1,eps3,d,ak0,a,r,trp(2),z,z0,k0,k
      double complex  ::eps2
      double complex ::f11r(9),g11r(9)
      double precision ::pi,k11,cop,sip,co2p,CYR(2),CYI(2)&
     &	  ,ku,j0,j1,j10
      double complex ::cim,c0,r12s,r12p,r23s,r23p,fs(9),fp(9)&
     &	 ,gs(9),gp(9),coeff,ww1,ww2,ww3,w1,w2,w3,ch0,ch1,ch10 &
     &	 ,ck,f1(9),f2(9),g1(9),g2(9),rs,rp
      integer ::l,NZ,IERR
      double precision ::dbesj0,dbesj1
!----------------------------!
! definitions preliminaires  !
!----------------------------!
	c0=dcmplx(0.d0,0d0)
	cim=dcmplx(0.d0,1.d0)
	pi=4.d0*datan(1.d0)
	k11=eps1*ak0*ak0
	cop=trp(1)
	sip=trp(2)
	co2p=cop*cop-sip*sip
!================================================
! cas ou r=0
! integration le lg axe reel
!================================================
	if (r .lt. 0.001d0) then 
	   ku=k0+k
! initialisation
	   do l=1,9
	      fs(l)=c0
	      fp(l)=c0
              gs(l)=c0
              gp(l)=c0
	   enddo
! vecteurs d'ondes dans chaque region
	   ww1=eps1*ak0*ak0-ku*ku
	   ww2=eps2*ak0*ak0-ku*ku
	   ww3=eps3*ak0*ak0-ku*ku
	   w1=cdsqrt(ww1)
	   w2=cdsqrt(ww2)
	   w3=cdsqrt(ww3)
	   if (dimag(w1) .lt. 0.d0) then
	      w1=-w1
	   endif
	   if (dimag(w2) .lt. 0.d0) then
	      w2=-w2
	   endif
	   if (dimag(w3) .lt. 0.d0) then
	      w3=-w3
	   endif
! coeff de Fresnel
! reflexion aux interfaces
	   r12s=(w1-w2)/(w1+w2)
	   r23s=(w2-w3)/(w2+w3)
	   r12p=(eps2*w1-eps1*w2)/(eps2*w1+eps1*w2)
	   r23p=(eps3*w2-eps2*w3)/(eps3*w2+eps2*w3)
! bilan reflexion 
        rs=(r12s+r23s*cdexp(2.d0*cim*w2*d))/&
     &       (1.d0+r12s*r23s*cdexp(2.d0*cim*w2*d))
	rp=(r12p+r23p*cdexp(2.d0*cim*w2*d))/&
     &       (1.d0+r12p*r23p*cdexp(2.d0*cim*w2*d))
!coeff des ondes planes
        coeff=cdexp(cim*w1*(z+z0))
! propagateur electrique
!1ere ligne
	fs(1)=0.5d0*k11*ku*rs/w1
	fp(1)=-0.5d0*w1*ku*rp
!2eme ligne
	fs(5)=fs(1)
	fp(5)=fp(1)
! 3eme ligne
	fp(9)=ku*ku*ku*rp/w1
! propagateur mixte
!1ere ligne
	gs(2)=0.5d0*ku*rs
	gp(2)=0.5d0*ku*rp
!2eme ligne
	gs(4)=0.5d0*ku*rs
	gp(4)=-0.5d0*ku*rp
! 3eme ligne
        do l=1,9
           f11r(l)=(fs(l)+fp(l))*cim*coeff/eps1
           g11r(l)=(gs(l)+gp(l))*cim*coeff
        enddo
	else
!================================================
! cas ou z-z0 > 50 nm 
! utilisation des fonctions de Bessel (calcul plus rapide)
!===============================================
! integration lg axe reel
!===============================================
	   ku=k0+k
! initialisation
	   do l=1,9
	      fs(l)=c0
	      fp(l)=c0
              gs(l)=c0
              gp(l)=c0
	   enddo
! fonctions de Bessel
	   j0=dbesj0(ku*r)
	   j1=dbesj1(ku*r)
	   j10=j1/(ku*r)
! vecteurs d'ondes dans chaque region
	   ww1=eps1*ak0*ak0-ku*ku
	   ww2=eps2*ak0*ak0-ku*ku
	   ww3=eps3*ak0*ak0-ku*ku
	   w1=cdsqrt(ww1)
	   w2=cdsqrt(ww2)
	   w3=cdsqrt(ww3)
	   if (dimag(w1) .lt. 0.d0) then
	      w1=-w1
	   endif
	   if (dimag(w2) .lt. 0.d0) then
	      w2=-w2
	   endif
	   if (dimag(w3) .lt. 0.d0) then
	      w3=-w3
	   endif
! coeff de Fresnel
! reflexion aux interfaces
	   r12s=(w1-w2)/(w1+w2)
	   r23s=(w2-w3)/(w2+w3)
	   r12p=(eps2*w1-eps1*w2)/(eps2*w1+eps1*w2)
	   r23p=(eps3*w2-eps2*w3)/(eps3*w2+eps2*w3)
! bilan reflexion 
	rs=(r12s+r23s*cdexp(2.d0*cim*w2*d))/&
     &       (1.d0+r12s*r23s*cdexp(2.d0*cim*w2*d))
	rp=(r12p+r23p*cdexp(2.d0*cim*w2*d))/&
     &       (1.d0+r12p*r23p*cdexp(2.d0*cim*w2*d))
!coeff des ondes planes
        coeff=cdexp(cim*w1*(z+z0))
! propagateur electrique
!1ere ligne
	fs(1)=k11*ku*rs*(sip*sip*j0+co2p*j10)/w1
	fp(1)=-w1*ku*rp*(cop*cop*j0-co2p*j10)
	fs(2)=-k11*ku*rs*sip*cop*(j0-2.d0*j10)/w1
	fp(2)=-w1*ku*rp*sip*cop*(j0-2.d0*j10)
	fp(3)=-cim*ku*ku*rp*cop*j1
!2eme ligne
	fs(5)=k11*ku*rs*(cop*cop*j0-co2p*j10)/w1
	fp(5)=-w1*ku*rp*(sip*sip*j0+co2p*j10)
	fp(6)=-cim*ku*ku*rp*sip*j1
! 3eme ligne
	fp(7)=cim*ku*ku*cop*rp*j1
	fp(8)=cim*ku*ku*sip*rp*j1
	fp(9)=ku*ku*ku*rp*j0/w1
! propagateur mixte
!1ere ligne
	gs(1)=ku*rs*sip*cop*(j0-2.d0*j10)
	gp(1)=ku*rp*sip*cop*(j0-2.d0*j10)
	gs(2)=ku*rs*(cop*cop*j0-co2p*j10)
	gp(2)=ku*rp*(sip*sip*j0+co2p*j10)
	gp(3)=cim*rp*ku*ku*sip*j1/w1
!2eme ligne
	gs(4)=ku*rs*(sip*sip*j0+co2p*j10)
	gp(4)=-ku*rp*(cop*cop*j0-co2p*j10)
	gp(6)=-cim*rp*ku*ku*cop*j1/w1
! 3eme ligne
	gs(7)=-cim*rs*ku*ku*sip*j1/w1
	gs(8)=cim*rs*ku*ku*cop*j1/w1
! reconstruction
        do l=1,9
           f11r(l)=(fs(l)+fp(l))*coeff*cim/eps1
           g11r(l)=(gs(l)+gp(l))*coeff*cim
        enddo
	endif
	RETURN
	END

























!!-------------------------------------------------------------------!
! propagateur de surface retarde S13                                 !
!--------------------------------------------------------------------!
	SUBROUTINE PROPAG13(eps1,eps2,eps3,d,ak0,a,xd,yd,z,z0,s13)
	implicit none
	double precision::prec=1.d-6
	double precision::eps1,eps3,d,ak0,a,xd,yd,z,z0
	double complex  ::eps2
	double complex, intent(out) ::s13(9)
	double precision ::pi,r,phi,trp(2),ki(3),kmax,kmaj,kmin&
     &	 ,k,t,dt,dk,n3,k3,wg(4),kinfinity&
     &   ,xgk(8),wgk(8),resabs(9),t0,t1,centr,hlgth,dhlgth,absc&
     &	 ,k0,k1,err0,abserr0
	double complex ::cim,c0,ck,dck,fc(9),resg(9),resk(9)&
     &	 ,fval1(9),fval2(9),fv1(7,9),fv2(7,9),fsum(9)


	integer ::l,nt,j,jtw,jtwm1

!----------------------------!
! definitions preliminaires  !
!----------------------------!
	c0=dcmplx(0.d0,0d0)
	cim=dcmplx(0.d0,1.d0)
	pi=4.d0*datan(1.d0)
! coordonnees cylindriques
	r=dsqrt(xd*xd+yd*yd)
	if (r .lt. a/2.d0) then
	   r=0.d0
	   phi=0.d0
	elseif (dabs(xd) .lt. a/2.d0) then
	   if (yd .ge. 0.d0) then 
	      phi=pi/2.d0
	   else 
	      phi=-pi/2.d0
	   endif
	elseif (dabs(yd) .lt. a/2.d0) then
	   if (xd .ge. 0.d0) then 
	      phi=0.d0
	   else 
	      phi=-pi
	   endif
	else
	   if (xd .ge. 0.d0) then 
	      phi=datan(yd/xd)
	   elseif (xd .le. 0.d0) then
	      phi=datan(yd/xd)+pi
	   else
	      write(*,*)'probleme ds definition coord. cyl. !'
	   endif 
	endif
	trp(1)=dcos(phi)
	trp(2)=dsin(phi)
! initialisation propagateur
	do l=1,9
	   s13(l)=c0
	enddo
! definition du chemin d'integration
! integration le long de k_parrallele
! contournement des singularites
	ki(1)=dsqrt(eps1)*ak0
	ki(2)=dble(cdsqrt(eps2)*ak0)
	ki(3)=dsqrt(eps3)*ak0
	kmax=0.d0
	do l=1,3
	   if (ki(l) .gt. kmax) then 
	      kmax=ki(l)
	   endif
	enddo
	kmaj=(ak0+kmax)/2.d0
	kmin=0.001d0*kmaj
!==============================================
! Algorithme de Gauss Kronrod
! coefficients 
	WG(1)=0.129484966168869693270611432679082d0
	WG(2)=0.279705391489276667901467771423780d0
	WG(3)=0.381830050505118944950369775488975d0
	WG(4)=0.417959183673469387755102040816327d0
!
	XGK(1)=0.991455371120812639206854697526329d0
	XGK(2)=0.949107912342758524526189684047851d0
	XGK(3)=0.864864423359769072789712788640926d0
	XGK(4)=0.741531185599394439863864773280788d0
	XGK(5)=0.586087235467691130294144838258730d0
	XGK(6)=0.405845151377397166906606412076961d0
	XGK(7)=0.207784955007898467600689403773245d0
	XGK(8)=0.000000000000000000000000000000000d0
!
	WGK(1)=0.022935322010529224963732008058970d0
	WGK(2)=0.063092092629978553290700663189204d0
	WGK(3)=0.104790010322250183839876322541518d0
	WGK(4)=0.140653259715525918745189590510238d0
	WGK(5)=0.169004726639267902826583426598550d0
	WGK(6)=0.190350578064785409913256402421014d0
	WGK(7)=0.204432940075298892414161999234649d0
	WGK(8)=0.209482141084727828012999174891714d0
!
!***FIRST EXECUTABLE STATEMENT  DQK15
!
! integration dans le plan complexe (t entre 0 et pi)
	nt=0
	t0=0.d0
	t1=pi
 25	nt=nt+1
        centr = 0.5d+00*(t0+t1)
	hlgth = 0.5d+00*(t1-t0)
	dhlgth = dabs(hlgth)
!
!           compute the 15-point kronrod approximation to
!           the integral, and estimate the absolute error.
!
        ck=dcmplx(kmaj-kmaj*dcos(centr),-kmin*dsin(centr))
	dck=dcmplx(kmaj*dsin(centr),-kmin*dcos(centr))
        call FC13(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,fc)
	do l=1,9
	   resg(l) = fc(l)*wg(4)
	   resk(l) = fc(l)*wgk(8)
	enddo
	do 10 j=1,3
	   jtw = j*2
	   absc = hlgth*xgk(jtw)
	   t=centr-absc
	   ck=dcmplx(kmaj-kmaj*dcos(t),-kmin*dsin(t))
	   dck=dcmplx(kmaj*dsin(t),-kmin*dcos(t))
	call FC13(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,fval1)
	   t=centr+absc
	   ck=dcmplx(kmaj-kmaj*dcos(t),-kmin*dsin(t))
	   dck=dcmplx(kmaj*dsin(t),-kmin*dcos(t))
        call FC13(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,fval2)
        do l=1,9
           fv1(jtw,l) = fval1(l)
           fv2(jtw,l) = fval2(l)
           fsum(l) = fval1(l)+fval2(l)
           resg(l) = resg(l)+wg(j)*fsum(l)
           resk(l) = resk(l)+wgk(jtw)*fsum(l)
        enddo
 10	CONTINUE
	DO 15 j = 1,4
	   jtwm1 = j*2-1
	   absc = hlgth*xgk(jtwm1)
	   t=centr-absc
	   ck=dcmplx(kmaj-kmaj*dcos(t),-kmin*dsin(t))
	   dck=dcmplx(kmaj*dsin(t),-kmin*dcos(t))
	call FC13(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,fval1)
        t=centr+absc
        ck=dcmplx(kmaj-kmaj*dcos(t),-kmin*dsin(t))
        dck=dcmplx(kmaj*dsin(t),-kmin*dcos(t))
	call FC13(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,fval2)
        do l=1,9
           fv1(jtwm1,l) = fval1(l)
           fv2(jtwm1,l) = fval2(l)
           fsum(l) = fval1(l)+fval2(l)
           resk(l) = resk(l)+wgk(jtwm1)*fsum(l)
        enddo
 15	CONTINUE
	abserr0=0.d0
	err0=0.d0
	do l=1,9
	   abserr0=abserr0+cdabs((resk(l)-resg(l)))*hlgth
           err0=err0+cdabs(s13(l)+resk(l)*hlgth)
	enddo
        abserr0=abserr0/err0
	if ((abserr0) .le. prec) then 
	   do l=1,9
	      s13(l)=s13(l)+resk(l)*hlgth
	   enddo
	   if (t1 .lt. pi) then
	      t0=t1
	      t1=pi
	      goto 25 
	   endif
	else
	   t1=centr
	   goto 25
	endif
! poursuite de l'integration le long axe reel
	nt=0
	kinfinity=500.d0*kmaj
	k0=0.d0
	k1=kinfinity
 300	nt=nt+1
        centr = 0.5d+00*(k0+k1)
	hlgth = 0.5d+00*(k1-k0)
	dhlgth = dabs(hlgth)
!
!           compute the 15-point kronrod approximation to
!           the integral, and estimate the absolute error.
!
      call FR13(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,2.d0*kmaj,centr,fc)
      do l=1,9
         resg(l) = fc(l)*wg(4)
         resk(l) = fc(l)*wgk(8)
      enddo
      do 100 j=1,3
        jtw = j*2
        absc = hlgth*xgk(jtw)
	k=centr-absc
      call FR13(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,2.d0*kmaj,k,fval1)
	k=centr+absc
      call FR13(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,2.d0*kmaj,k,fval2)
      do l=1,9
         fv1(jtw,l) = fval1(l)
         fv2(jtw,l) = fval2(l)
         fsum(l) = fval1(l)+fval2(l)
         resg(l) = resg(l)+wg(j)*fsum(l)
         resk(l) = resk(l)+wgk(jtw)*fsum(l)
      enddo
 100  CONTINUE
      DO 150 j = 1,4
	jtwm1 = j*2-1
	absc = hlgth*xgk(jtwm1)
	k=centr-absc
      call FR13(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,2.d0*kmaj,k,fval1)
      k=centr+absc
      call FR13(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,2.d0*kmaj,k,fval2)
      do l=1,9
         fv1(jtwm1,l) = fval1(l)
         fv2(jtwm1,l) = fval2(l)
         fsum(l) = fval1(l)+fval2(l)
         resk(l) = resk(l)+wgk(jtwm1)*fsum(l)
      enddo
 150  CONTINUE
      abserr0=0.d0
      err0=0.d0
      do l=1,9
         abserr0=abserr0+cdabs((resk(l)-resg(l)))*hlgth
         err0=err0+cdabs(s13(l)+resk(l)*hlgth)
      enddo
      abserr0=abserr0/err0
      if ((abserr0) .le. prec) then 
         do l=1,9
            s13(l)=s13(l)+resk(l)*hlgth
         enddo
         if (k1 .lt. kinfinity) then
            k0=k1
            k1=kinfinity
            goto 300 
         endif
      else
         k1=centr
         goto 300 
      endif
! proprietes de symetrie
      s13(4)=s13(2)
      RETURN     
      END
      
!======================================================!
!================================================================
      SUBROUTINE FC13(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,f13c)
      implicit none
      double precision::eps1,eps3,d,ak0,a,r,trp(2),z,z0
      double complex  ::eps2,ck,dck
      double complex ::f13c(9)
      double precision ::pi,n13,k11,cop,sip,co2p,CYR(2),CYI(2),n1,n3
      double complex   ::cim,c0,r12s,r12p,r23s,r23p,fs(9),fp(9),ts,tp,n2&
     &	 ,cj0,cj1,cj10,coeff,ww1,ww2,ww3,w1,w2,w3,t12s,t12p,t23s,t23p
      integer                    ::l,NZ,IERR
!----------------------------!
! definitions preliminaires  !
!----------------------------!
	c0=dcmplx(0.d0,0d0)
	cim=dcmplx(0.d0,1.d0)
	pi=4.d0*datan(1.d0)
	n13=dsqrt(eps1/eps3)
	n1=dsqrt(eps1)
	n2=cdsqrt(eps2)
	n3=dsqrt(eps3)
	k11=eps1*ak0*ak0
	cop=trp(1)
	sip=trp(2)
	co2p=cop*cop-sip*sip
! initialisation
	do l=1,9
	   fs(l)=c0
	   fp(l)=c0
	enddo
! fonctions de Bessel
	if (r .lt. 0.001d0) then
	   cj0=dcmplx(1.d0,0.d0)
	   cj1=c0
	   cj10=dcmplx(0.5d0,0.d0)
	else
        call ZBESJ(dble(ck*r),dimag(ck*r),0,1,2,CYR,CYI,NZ,IERR)
        cj0=dcmplx(CYR(1),CYI(1))
        cj1=dcmplx(CYR(2),CYI(2))
        cj10=cj1/(ck*r)
	endif
! vecteurs d'ondes dans chaque region
	ww1=eps1*ak0*ak0-ck*ck
	ww2=eps2*ak0*ak0-ck*ck
	ww3=eps3*ak0*ak0-ck*ck
	w1=cdsqrt(ww1)
	w2=cdsqrt(ww2)
	w3=cdsqrt(ww3)
	if (dimag(w1) .lt. 0.d0) then
	   w1=-w1
	endif
	if (dimag(w2) .lt. 0.d0) then
	   w2=-w2
	endif
	if (dimag(w3) .lt. 0.d0) then
	   w3=-w3
	endif
! coeff de Fresnel
! reflexion aux interfaces
	r12s=(w1-w2)/(w1+w2)
	r23s=(w2-w3)/(w2+w3)
	r12p=(eps2*w1-eps1*w2)/(eps2*w1+eps1*w2)
	r23p=(eps3*w2-eps2*w3)/(eps3*w2+eps2*w3)
	t12s=2.d0*w1/(w1+w2)
	t23s=2.d0*w2/(w2+w3)
	t12p=2.d0*n1*n2*w1/(eps2*w1+eps1*w2)
	t23p=2.d0*n2*n3*w2/(eps3*w2+eps2*w3)
! bilan transmission
	ts=(t12s*t23s*cdexp(cim*w2*d))/&
     &       (1.d0+r12s*r23s*cdexp(2.d0*cim*w2*d))
	tp=(t12p*t23p*cdexp(cim*w2*d))/&
     &       (1.d0+r12p*r23p*cdexp(2.d0*cim*w2*d))
!coeff des ondes planes
        coeff=ck*cdexp(cim*w1*z0)*cdexp(-cim*w3*(d+z))
! propagateur electrique
!1ere ligne
	fs(1)=k11*ts*(sip*sip*cj0+co2p*cj10)/w1
	fp(1)=n13*w3*tp*(cop*cop*cj0-co2p*cj10)
	fs(2)=-k11*ts**sip*cop*(cj0-2.d0*cj10)
	fp(2)=n13*w3*tp*sip*cop*(cj0-2.d0*cj10)
	fp(3)=cim*n13*w3*tp*cop*cj1/w1
!2eme ligne
	fs(5)=k11*ts*(cop*cop*cj0-co2p*cj10)/w1
	fp(5)=n13*w3*tp*(sip*sip*cj0+co2p*cj10)
	fp(6)=cim*n13*w3*tp*sip*cj1/w1
! 3eme ligne
	fp(7)=cim*n13*tp*ck*cop*cj1
	fp(8)=cim*n13*tp*ck*sip*cj1
	fp(9)=n13*ck**2*tp*cj0/w1
! reconstruction
	do l=1,9
	   f13c(l)=(fs(l)+fp(l))*coeff*cim*dck/eps1
	enddo
	RETURN
	END
!==========================================================
      SUBROUTINE FR13(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,k0,k,f13r)
      implicit none
      double precision::eps1,eps3,d,ak0,a,r,trp(2),z,z0,k0,k
      double complex  ::eps2
      double complex ::f13r(9)
      double precision ::pi,k11,n13,cop,sip,co2p,CYR(2),CYI(2)&
     &	  ,ku,j0,j1,j10,n1,n3
      double complex ::cim,c0,r12s,r12p,r23s,r23p,fs(9),fp(9)&
     &	 ,gs(9),gp(9),coeff,ww1,ww2,ww3,w1,w2,w3,ch0,ch1,ch10&
     &	 ,ck,f1(9),f2(9),ts,tp,t12s,t12p,t23s,t23p,n2
      integer ::l,NZ,IERR
      double precision ::dbesj0,dbesj1
!----------------------------!
! definitions preliminaires  !
!----------------------------!
	c0=dcmplx(0.d0,0d0)
	cim=dcmplx(0.d0,1.d0)
	pi=4.d0*datan(1.d0)
	k11=eps1*ak0*ak0
	n13=dsqrt(eps1/eps3)
	n1=dsqrt(eps1)
	n2=cdsqrt(eps2)
	n3=dsqrt(eps3)
	cop=trp(1)
	sip=trp(2)
	co2p=cop*cop-sip*sip
!================================================
! cas ou r=0
! integration le lg axe reel
!================================================
	if (r .lt. 0.001d0) then 
	   ku=k0+k
! initialisation
	   do l=1,9
	      fs(l)=c0
	      fp(l)=c0
	   enddo
! vecteurs d'ondes dans chaque region
	   ww1=eps1*ak0*ak0-ku*ku
	   ww2=eps2*ak0*ak0-ku*ku
	   ww3=eps3*ak0*ak0-ku*ku
	   w1=cdsqrt(ww1)
	   w2=cdsqrt(ww2)
	   w3=cdsqrt(ww3)
	   if (dimag(w1) .lt. 0.d0) then
	      w1=-w1
	   endif
	   if (dimag(w2) .lt. 0.d0) then
	      w2=-w2
	   endif
	   if (dimag(w3) .lt. 0.d0) then
	      w3=-w3
	   endif
! coeff de Fresnel
! reflexion aux interfaces
	   r12s=(w1-w2)/(w1+w2)
	   r23s=(w2-w3)/(w2+w3)
	   r12p=(eps2*w1-eps1*w2)/(eps2*w1+eps1*w2)
	   r23p=(eps3*w2-eps2*w3)/(eps3*w2+eps2*w3)
	   t12s=2.d0*w1/(w1+w2)
	   t23s=2.d0*w2/(w2+w3)
	   t12p=2.d0*n1*n2*w1/(eps2*w1+eps1*w2)
	   t23p=2.d0*n2*n3*w2/(eps3*w2+eps2*w3)
! bilan transmission
	   ts=(t12s*t23s*cdexp(cim*w2*d))/&
     &	  (1.d0+r12s*r23s*cdexp(2.d0*cim*w2*d))
	   tp=(t12p*t23p*cdexp(cim*w2*d))/&
     &	(1.d0+r12p*r23p*cdexp(2.d0*cim*w2*d))
!coeff des ondes planes
        coeff=ku*cdexp(cim*w1*z0)*cdexp(-cim*w3*(d+z))
! propagateur electrique
!1ere ligne
	fs(1)=0.5d0*k11*ts/w1
	fp(1)=0.5d0*n13*w3*tp
!2eme ligne
	fs(5)=fs(1)
	fp(5)=fp(1)
! 3eme ligne
	fp(9)=n13*ku**2*tp
        do l=1,9
           f13r(l)=(fs(l)+fp(l))*cim*coeff/eps1
        enddo
	else
!================================================
! cas ou z-z0 > 50 nm 
! utilisation des fonctions de Bessel (calcul plus rapide)
!===============================================
! integration lg axe reel
!===============================================
	   ku=k0+k
! initialisation
	   do l=1,9
	      fs(l)=c0
	      fp(l)=c0
	   enddo
! fonctions de Bessel
	   j0=dbesj0(ku*r)
	   j1=dbesj1(ku*r)
	   j10=j1/(ku*r)
! vecteurs d'ondes dans chaque region
	   ww1=eps1*ak0*ak0-ku*ku
	   ww2=eps2*ak0*ak0-ku*ku
	   ww3=eps3*ak0*ak0-ku*ku
	   w1=cdsqrt(ww1)
	   w2=cdsqrt(ww2)
	   w3=cdsqrt(ww3)
	   if (dimag(w1) .lt. 0.d0) then
	      w1=-w1
	   endif
	   if (dimag(w2) .lt. 0.d0) then
	      w2=-w2
	   endif
	   if (dimag(w3) .lt. 0.d0) then
	      w3=-w3
	   endif
! coeff de Fresnel
! reflexion aux interfaces
	   r12s=(w1-w2)/(w1+w2)
	   r23s=(w2-w3)/(w2+w3)
	   r12p=(eps2*w1-eps1*w2)/(eps2*w1+eps1*w2)
	   r23p=(eps3*w2-eps2*w3)/(eps3*w2+eps2*w3)
	   t12s=2.d0*w1/(w1+w2)
	   t23s=2.d0*w2/(w2+w3)
	   t12p=2.d0*n1*n2*w1/(eps2*w1+eps1*w2)
	   t23p=2.d0*n2*n3*w2/(eps3*w2+eps2*w3)
! bilan transmission
	   ts=(t12s*t23s*cdexp(cim*w2*d))/&
     &	  (1.d0+r12s*r23s*cdexp(2.d0*cim*w2*d))
	   tp=(t12p*t23p*cdexp(cim*w2*d))/&
     &	  (1.d0+r12p*r23p*cdexp(2.d0*cim*w2*d))
!coeff des ondes planes
        coeff=ku*cdexp(cim*w1*z0)*cdexp(-cim*w3*(d+z))
! propagateur electrique
!1ere ligne
!1ere ligne
	fs(1)=k11*ts*(sip*sip*j0+co2p*j10)/w1
	fp(1)=n13*w3*tp*(cop*cop*j0-co2p*j10)
	fs(2)=-k11*ts**sip*cop*(j0-2.d0*j10)
	fp(2)=n13*w3*tp*sip*cop*(j0-2.d0*j10)
	fp(3)=cim*n13*w3*tp*cop*j1/w1
!2eme ligne
	fs(5)=k11*ts*(cop*cop*j0-co2p*j10)/w1
	fp(5)=n13*w3*tp*(sip*sip*j0+co2p*j10)
	fp(6)=cim*n13*w3*tp*sip*j1/w1
! 3eme ligne
	fp(7)=cim*n13*tp*ku*cop*j1
	fp(8)=cim*n13*tp*ku*sip*j1
	fp(9)=n13*ku**2*tp*j0/w1
! reconstruction
        do l=1,9
           f13r(l)=(fs(l)+fp(l))*coeff*cim/eps1
        enddo
	endif
	RETURN
	END




















!!-------------------------------------------------------------------!
! propagateur de transmission S21                                    !
!--------------------------------------------------------------------!
	SUBROUTINE PROPAG21(eps1,eps2,eps3,d,ak0,a,xd,yd,z,z0,s21,q21)
	implicit none
	double precision::prec=1.d-6
	double precision::eps1,eps3,d,ak0,a,xd,yd,z,z0
	double complex  ::eps2
	double complex, intent(out) ::s21(9),q21(9)
	double precision ::pi,r,phi,trp(2),ki(3),kmax,kmaj,kmin&
     &	 ,k,t,dt,dk,n3,k3,wg(4),kinfinity&
     &   ,xgk(8),wgk(8),resabs(9),t0,t1,centr,hlgth,dhlgth,absc&
     &	 ,k0,k1,abserr0,err0
	double complex ::cim,c0,ck,dck,fc(9),resg(9),resk(9)&
     &	 ,fval1(9),fval2(9),fv1(7,9),fv2(7,9),fsum(9),gsum(9)&
     &	 ,gc(9),bresg(9),bresk(9),gval1(9),gval2(9),gv1(7,9),gv2(7,9)
	integer ::l,nt,j,jtw,jtwm1

!----------------------------!
! definitions preliminaires  !
!----------------------------!
	c0=dcmplx(0.d0,0d0)
	cim=dcmplx(0.d0,1.d0)
	pi=4.d0*datan(1.d0)
! coordonnees cylindriques
	r=dsqrt(xd*xd+yd*yd)
	if (r .lt. a/2.d0) then
	   r=0.d0
	   phi=0.d0
	elseif (dabs(xd) .lt. a/2.d0) then
	   if (yd .ge. 0.d0) then 
	      phi=pi/2.d0
	   else 
	      phi=-pi/2.d0
	   endif
	elseif (dabs(yd) .lt. a/2.d0) then
	   if (xd .ge. 0.d0) then 
	      phi=0.d0
	   else 
	      phi=-pi
	   endif
	else
	   if (xd .ge. 0.d0) then 
	      phi=datan(yd/xd)
	   elseif (xd .le. 0.d0) then
	      phi=datan(yd/xd)+pi
	   else
	      write(*,*)'probleme ds definition coord. cyl. !'
	   endif 
	endif
	trp(1)=dcos(phi)
	trp(2)=dsin(phi)
! initialisation propagateur
	do l=1,9
	   s21(l)=c0
	   q21(l)=c0
	enddo
! definition du chemin d'integration
! integration le long de k_parrallele
! contournement des singularites
	ki(1)=dsqrt(eps1)*ak0
	ki(2)=dble(cdsqrt(eps2)*ak0)
	ki(3)=dsqrt(eps3)*ak0
	kmax=0.d0
	do l=1,3
	   if (ki(l) .gt. kmax) then 
	      kmax=ki(l)
	   endif
	enddo
	kmaj=(ak0+kmax)/2.d0
	kmin=0.001d0*kmaj
!==============================================
! Algorithme de Gauss Kronrod
! coefficients 
	WG(1)=0.129484966168869693270611432679082d0
	WG(2)=0.279705391489276667901467771423780d0
	WG(3)=0.381830050505118944950369775488975d0
	WG(4)=0.417959183673469387755102040816327d0
!
	XGK(1)=0.991455371120812639206854697526329d0
	XGK(2)=0.949107912342758524526189684047851d0
	XGK(3)=0.864864423359769072789712788640926d0
	XGK(4)=0.741531185599394439863864773280788d0
	XGK(5)=0.586087235467691130294144838258730d0
	XGK(6)=0.405845151377397166906606412076961d0
	XGK(7)=0.207784955007898467600689403773245d0
	XGK(8)=0.000000000000000000000000000000000d0
!
	WGK(1)=0.022935322010529224963732008058970d0
	WGK(2)=0.063092092629978553290700663189204d0
	WGK(3)=0.104790010322250183839876322541518d0
	WGK(4)=0.140653259715525918745189590510238d0
	WGK(5)=0.169004726639267902826583426598550d0
	WGK(6)=0.190350578064785409913256402421014d0
	WGK(7)=0.204432940075298892414161999234649d0
	WGK(8)=0.209482141084727828012999174891714d0
!
!***FIRST EXECUTABLE STATEMENT  DQK15
!
! integration dans le plan complexe (t entre 0 et pi)
	nt=0
	t0=0.d0
	t1=pi
 25	nt=nt+1
        centr = 0.5d+00*(t0+t1)
	hlgth = 0.5d+00*(t1-t0)
	dhlgth = dabs(hlgth)
!
!           compute the 15-point kronrod approximation to
!           the integral, and estimate the absolute error.
!
        ck=dcmplx(kmaj-kmaj*dcos(centr),-kmin*dsin(centr))
	dck=dcmplx(kmaj*dsin(centr),-kmin*dcos(centr))
        call FC21(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,fc,gc)
	do l=1,9
	   resg(l) = fc(l)*wg(4)
	   resk(l) = fc(l)*wgk(8)
	   bresg(l) = gc(l)*wg(4)
	   bresk(l) = gc(l)*wgk(8)
	enddo
	do 10 j=1,3
	   jtw = j*2
	   absc = hlgth*xgk(jtw)
	   t=centr-absc
	   ck=dcmplx(kmaj-kmaj*dcos(t),-kmin*dsin(t))
	   dck=dcmplx(kmaj*dsin(t),-kmin*dcos(t))
	call FC21(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,fval1,gval1)
	   t=centr+absc
	   ck=dcmplx(kmaj-kmaj*dcos(t),-kmin*dsin(t))
	   dck=dcmplx(kmaj*dsin(t),-kmin*dcos(t))
        call FC21(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,fval2,gval2)
        do l=1,9
           fv1(jtw,l) = fval1(l)
           fv2(jtw,l) = fval2(l)
           fsum(l) = fval1(l)+fval2(l)
           resg(l) = resg(l)+wg(j)*fsum(l)
           resk(l) = resk(l)+wgk(jtw)*fsum(l)
!
           gv1(jtw,l) = gval1(l)
           gv2(jtw,l) = gval2(l)
           gsum(l) = gval1(l)+gval2(l)
           bresg(l) = bresg(l)+wg(j)*gsum(l)
           bresk(l) = bresk(l)+wgk(jtw)*gsum(l)
        enddo
 10	CONTINUE
	DO 15 j = 1,4
	   jtwm1 = j*2-1
	   absc = hlgth*xgk(jtwm1)
	   t=centr-absc
	   ck=dcmplx(kmaj-kmaj*dcos(t),-kmin*dsin(t))
	   dck=dcmplx(kmaj*dsin(t),-kmin*dcos(t))
	call FC21(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,fval1,gval1)
        t=centr+absc
        ck=dcmplx(kmaj-kmaj*dcos(t),-kmin*dsin(t))
        dck=dcmplx(kmaj*dsin(t),-kmin*dcos(t))
	call FC21(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,fval2,gval2)
        do l=1,9
           fv1(jtwm1,l) = fval1(l)
           fv2(jtwm1,l) = fval2(l)
           fsum(l) = fval1(l)+fval2(l)
           resk(l) = resk(l)+wgk(jtwm1)*fsum(l)
!
           gv1(jtwm1,l) = gval1(l)
           gv2(jtwm1,l) = gval2(l)
           gsum(l) = gval1(l)+gval2(l)
           bresk(l) = bresk(l)+wgk(jtwm1)*gsum(l)
        enddo
 15	CONTINUE
	abserr0=0.d0
        err0=0.d0
	do l=1,9
	   abserr0=abserr0+cdabs((resk(l)-resg(l)))*hlgth
!     &          +cdabs((bresk(l)-bresg(l)))*hlgth
           err0=err0+cdabs(s21(l)+resk(l)*hlgth)
!     &          +cdabs(q21(l)+bresk(l)*hlgth)
	enddo
        abserr0=abserr0/err0
	if ((abserr0) .le. prec) then 
	   do l=1,9
	      s21(l)=s21(l)+resk(l)*hlgth
	      q21(l)=q21(l)+bresk(l)*hlgth
	   enddo
	   if (t1 .lt. pi) then
	      t0=t1
	      t1=pi
	      goto 25 
	   endif
	else
	   t1=centr
	   goto 25
	endif
! poursuite de l'integration le long axe reel
	nt=0
	kinfinity=500.d0*kmaj
	k0=0.d0
	k1=kinfinity
 300	nt=nt+1
        centr = 0.5d+00*(k0+k1)
	hlgth = 0.5d+00*(k1-k0)
	dhlgth = dabs(hlgth)
!
!           compute the 15-point kronrod approximation to
!           the integral, and estimate the absolute error.
!
      call FR21(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,2.d0*kmaj,&
     &       centr,fc,gc)
      do l=1,9
         resg(l) = fc(l)*wg(4)
         resk(l) = fc(l)*wgk(8)
         bresg(l) = gc(l)*wg(4)
         bresk(l) = gc(l)*wgk(8)
      enddo
      do 100 j=1,3
        jtw = j*2
        absc = hlgth*xgk(jtw)
	k=centr-absc
      call FR21(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,2.d0*kmaj,k,&
     &       fval1,gval1)
	k=centr+absc
      call FR21(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,2.d0*kmaj,k,&
     &       fval2,gval2)
      do l=1,9
         fv1(jtw,l) = fval1(l)
         fv2(jtw,l) = fval2(l)
         fsum(l) = fval1(l)+fval2(l)
         resg(l) = resg(l)+wg(j)*fsum(l)
         resk(l) = resk(l)+wgk(jtw)*fsum(l)
!
         gv1(jtw,l) = gval1(l)
         gv2(jtw,l) = gval2(l)
         gsum(l) = gval1(l)+gval2(l)
         bresg(l) = bresg(l)+wg(j)*gsum(l)
         bresk(l) = bresk(l)+wgk(jtw)*gsum(l)
      enddo
 100  CONTINUE
      DO 150 j = 1,4
	jtwm1 = j*2-1
	absc = hlgth*xgk(jtwm1)
	k=centr-absc
      call FR21(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,2.d0*kmaj,k,&
     &       fval1,gval1)
      k=centr+absc
      call FR21(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,2.d0*kmaj,k,&
     &     fval2,gval2)
      do l=1,9
         fv1(jtwm1,l) = fval1(l)
         fv2(jtwm1,l) = fval2(l)
         fsum(l) = fval1(l)+fval2(l)
         resk(l) = resk(l)+wgk(jtwm1)*fsum(l)
!
         gv1(jtwm1,l) = gval1(l)
         gv2(jtwm1,l) = gval2(l)
         gsum(l) = gval1(l)+gval2(l)
         bresk(l) = bresk(l)+wgk(jtwm1)*gsum(l)
      enddo
 150  CONTINUE
      abserr0=0.d0
      err0=0.d0
      do l=1,9
         abserr0=abserr0+cdabs((resk(l)-resg(l)))*hlgth&
     &          +cdabs((bresk(l)-bresg(l)))*hlgth
         err0=err0+cdabs(s21(l)+resk(l)*hlgth)
!     &        +cdabs(q21(l)+bresk(l)*hlgth)

      enddo
      abserr0=abserr0/err0
      if ((abserr0) .le. prec) then 
         do l=1,9
            s21(l)=s21(l)+resk(l)*hlgth
            q21(l)=q21(l)+bresk(l)*hlgth
         enddo
         if (k1 .lt. kinfinity) then
            k0=k1
            k1=kinfinity
            goto 300 
         endif
      else
         k1=centr
         goto 300 
      endif
! proprietes de symetrie
      s21(4)=s21(2)
      q21(5)=-q21(1)
      q21(9)=c0
      RETURN     
      END
!======================================================!
!================================================================
      SUBROUTINE FC21(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,ck,dck,&
     &     f21c,g21c)
      implicit none
      double precision::eps1,eps3,d,ak0,a,r,trp(2),z,z0
      double complex  ::eps2,ck,dck
      double complex ::f21c(9),g21c(9)
      double precision ::pi,cop,sip,co2p,CYR(2),CYI(2),n1,k1
      double complex   ::cim,c0,r1s,r12s,r12p,r23s,r23p&
     &	 ,t21s,t21p,t1p,t1s,t2p,t2s,q1,q2,m1,s2,fs(9),fp(9),gs(9),gp(9)&
     &	 ,k22,cn21,cj0,cj1,cj10,coeff,ww1,ww2,ww3,w1,w2,w3,n2,k2
      integer                    ::l,NZ,IERR
!----------------------------!
! definitions preliminaires  !
!----------------------------!
	c0=dcmplx(0.d0,0d0)
	cim=dcmplx(0.d0,1.d0)
	pi=4.d0*datan(1.d0)
	k22=eps2*ak0*ak0
	n2=cdsqrt(eps2)
	n1=dsqrt(eps1)
	k2=n2*ak0
	k1=n1*ak0
	cn21=n2/n1
	cop=trp(1)
	sip=trp(2)
	co2p=cop*cop-sip*sip
! initialisation
	do l=1,9
	   fs(l)=c0
	   fp(l)=c0
	   gs(l)=c0
	   gp(l)=c0
	enddo
! fonctions de Bessel
	if (r .lt. 0.001d0) then
	   cj0=dcmplx(1.d0,0.d0)
	   cj1=c0
	   cj10=dcmplx(0.5d0,0.d0)
	else
        call ZBESJ(dble(ck*r),dimag(ck*r),0,1,2,CYR,CYI,NZ,IERR)
        cj0=dcmplx(CYR(1),CYI(1))
        cj1=dcmplx(CYR(2),CYI(2))
        cj10=cj1/(ck*r)
	endif
! vecteurs d'ondes dans chaque region
	ww1=eps1*ak0*ak0-ck*ck
	ww2=eps2*ak0*ak0-ck*ck
	ww3=eps3*ak0*ak0-ck*ck
	w1=cdsqrt(ww1)
	w2=cdsqrt(ww2)
	w3=cdsqrt(ww3)
	if (dimag(w1) .lt. 0.d0) then
	   w1=-w1
	endif
	if (dimag(w2) .lt. 0.d0) then
	   w2=-w2
	endif
	if (dimag(w3) .lt. 0.d0) then
	   w3=-w3
	endif
! coeff de Fresnel
! reflexion aux interfaces
	r12s=(w1-w2)/(w1+w2)
	r23s=(w2-w3)/(w2+w3)
	r12p=(eps2*w1-eps1*w2)/(eps2*w1+eps1*w2)
	r23p=(eps3*w2-eps2*w3)/(eps3*w2+eps2*w3)
! transmission interface 21
	t21s=2.d0*w2/(w2+w1)
	t21p=2.d0*n2*n1*w2/(eps2*w1+eps1*w2)
! bilan des transmissions
	q2=cdexp(2.d0*cim*w2*d)
	t1s=t21s/(1.d0+r12s*r23s*q2)
	t2s=t1s*r23s*q2
	t1p=t21p/(1.d0+r12p*r23p*q2)
	t2p=t1p*r23p*q2
!coeff des ondes planes
        coeff=cdexp(cim*w2*z0)
	q1=t1p/coeff-t2p*coeff
	q2=t1p/coeff+t2p*coeff
	m1=t1s/coeff+t2s*coeff
        coeff=cdexp(cim*w1*z)/eps2
! propagateur electrique
!1ere ligne
	fs(1)=k22*ck*m1*(sip*sip*cj0+co2p*cj10)/w2
	fp(1)=cn21*w1*ck*q1*(cop*cop*cj0-co2p*cj10)
	fs(2)=-k22*ck*m1*sip*cop*(cj0-2.d0*cj10)/w2
	fp(2)=cn21*w1*ck*q1*sip*cop*(cj0-2.d0*cj10)
	fp(3)=-cim*cn21*w1*ck*ck*cop*cj1*q2/w2
!2eme ligne
	fs(5)=k22*ck*m1*(cop*cop*cj0-co2p*cj10)/w2
	fp(5)=cn21*w1*ck*q1*(sip*sip*cj0+co2p*cj10)
	fp(6)=-cim*cn21*w1*ck*ck*sip*cj1*q2/w2
! 3eme ligne
	fp(7)=-cim*cn21*ck*ck*cop*cj1*q1
	fp(8)=-cim*cn21*ck*ck*sip*cj1*q1
	fp(9)=cn21*ck*ck*ck*cj0*q2/w2
! propagateur mixte
!1ere ligne
	gs(1)=k2*ck*m1*w1*sip*cop*(cj0-2.d0*cj10)/w2
	gp(1)=-k1*ck*q1*sip*cop*(cj0-2.d0*cj10)
	gs(2)=-k2*ck*w1*m1*(cop*cop*cj0-co2p*cj10)/w2
	gp(2)=-k1*ck*q1*(sip*sip*cj0+co2p*cj10)
	gp(3)=cim*k1*ck*ck*q2*sip*cj1/w2
!2eme ligne
	gs(4)=k2*ck*w1*m1*(sip*sip*cj0+co2p*cj10)/w2
	gp(4)=k1*ck*q1*(cop*cop*cj0-co2p*cj10)
	gp(6)=-cim*k1*ck*ck*q2*cop*cj1/w2
! 3eme ligne
	gs(7)=-cim*k2*ck*ck*m1*sip*cj1/w2
	gs(8)=cim*k2*ck*ck*m1*cop*cj1/w2
! reconstruction
	do l=1,9
	   f21c(l)=(fs(l)+fp(l))*coeff*cim*dck
	   g21c(l)=(gs(l)+gp(l))*coeff*cim*n2*dck
	enddo
	RETURN
	END
	
	
	
!==========================================================
      SUBROUTINE FR21(eps1,eps2,eps3,d,ak0,a,r,trp,z,z0,k0,k,f21r,g21r)
      implicit none
      double precision::eps1,eps3,d,ak0,a,r,trp(2),z,z0,k0,k
      double complex  ::eps2
      double complex ::f21r(9),g21r(9)
      double precision ::pi,cop,sip,co2p,CYR(2),CYI(2)&
     &	  ,ku,j0,j1,j10,n1,k1
      double complex ::cim,c0,r1s,r12s,r12p,r23s,r23p&
     &	 ,t21s,t21p,t1p,t1s,t2p,t2s,q1,q2,m1,s2,fs(9),fp(9),gs(9),gp(9)&
     &	 ,k22,cn21,coeff,ww1,ww2,ww3,w1,w2,w3,n2,k2,ch0,ch1,ch10 &
     &	 ,ck,f1(9),f2(9),g1(9),g2(9)
      integer ::l,NZ,IERR
      double precision ::dbesj0,dbesj1
!----------------------------!
! definitions preliminaires  !
!----------------------------!
	c0=dcmplx(0.d0,0d0)
	cim=dcmplx(0.d0,1.d0)
	pi=4.d0*datan(1.d0)
	k22=eps2*ak0*ak0
	n2=cdsqrt(eps2)
	n1=dsqrt(eps1)
	k2=n2*ak0
	k1=n1*ak0
	cn21=n2/n1
	cop=trp(1)
	sip=trp(2)
	co2p=cop*cop-sip*sip
!================================================
! cas ou r=0
! integration le lg axe reel
!================================================
	if (r .lt. 0.001d0) then 
	   ku=k0+k
! initialisation
	   do l=1,9
	      fs(l)=c0
	      fp(l)=c0
	      gs(l)=c0
	      gp(l)=c0
	   enddo
! vecteurs d'ondes dans chaque region
	   ww1=eps1*ak0*ak0-ku*ku
	   ww2=eps2*ak0*ak0-ku*ku
	   ww3=eps3*ak0*ak0-ku*ku
	   w1=cdsqrt(ww1)
	   w2=cdsqrt(ww2)
	   w3=cdsqrt(ww3)
	   if (dimag(w1) .lt. 0.d0) then
	      w1=-w1
	   endif
	   if (dimag(w2) .lt. 0.d0) then
	      w2=-w2
	   endif
	   if (dimag(w3) .lt. 0.d0) then
	      w3=-w3
	   endif
! coeff de Fresnel
! reflexion aux interfaces
	   r12s=(w1-w2)/(w1+w2)
	   r23s=(w2-w3)/(w2+w3)
	   r12p=(eps2*w1-eps1*w2)/(eps2*w1+eps1*w2)
	   r23p=(eps3*w2-eps2*w3)/(eps3*w2+eps2*w3)
! transmission interface 21
	   t21s=2.d0*w2/(w2+w1)
	   t21p=2.d0*n2*n1*w2/(eps2*w1+eps1*w2)
! bilan des transmissions
	   q2=cdexp(2.d0*cim*w2*d)
	   t1s=t21s/(1.d0+r12s*r23s*q2)
	   t2s=t1s*r23s*q2
	   t1p=t21p/(1.d0+r12p*r23p*q2)
	   t2p=t1p*r23p*q2
!coeff des ondes planes
           coeff=cdexp(cim*w2*z0)
	   q1=t1p/coeff-t2p*coeff
	   q2=t1p/coeff+t2p*coeff
	   m1=t1s/coeff+t2s*coeff
           coeff=cdexp(cim*w1*z)/eps2
! propagateur electrique
! 1ere ligne
	   fs(1)=0.5d0*k22*ku*m1/w2
	   fp(1)=0.5d0*cn21*ku*w1*q1
! 2eme ligne
	   fs(5)=fs(1)
	   fp(5)=fp(1)
! 3eme ligne
	   fp(9)=cn21*ku*ku*ku*q2/w2
! propagateur mixte
! 1ere ligne
	   gs(2)=-0.5d0*k2*ku*w1*m1/w2
	   gp(2)=-0.5d0*k1*ku*q1
! 2eme ligne
	   gs(4)=-gs(2)
	   gp(4)=-gp(2)
	   do l=1,9
	      f21r(l)=(fs(l)+fp(l))*cim*coeff
	      g21r(l)=(gs(l)+gp(l))*cim*n2*coeff
	   enddo
	else
!================================================
! cas ou z-z0 > 50 nm 
! utilisation des fonctions de Bessel (calcul plus rapide)
!===============================================
! integration lg axe reel
!===============================================
	   ku=k0+k
! initialisation
	   do l=1,9
	      fs(l)=c0
	      fp(l)=c0
	      gs(l)=c0
	      gp(l)=c0
	   enddo
! fonctions de Bessel
	   j0=dbesj0(ku*r)
	   j1=dbesj1(ku*r)
	   j10=j1/(ku*r)
! vecteurs d'ondes dans chaque region
	   ww1=eps1*ak0*ak0-ku*ku
	   ww2=eps2*ak0*ak0-ku*ku
	   ww3=eps3*ak0*ak0-ku*ku
	   w1=cdsqrt(ww1)
	   w2=cdsqrt(ww2)
	   w3=cdsqrt(ww3)
	   if (dimag(w1) .lt. 0.d0) then
	      w1=-w1
	   endif
	   if (dimag(w2) .lt. 0.d0) then
	      w2=-w2
	   endif
	   if (dimag(w3) .lt. 0.d0) then
	      w3=-w3
	   endif
! coeff de Fresnel
! reflexion aux interfaces
	   r12s=(w1-w2)/(w1+w2)
	   r23s=(w2-w3)/(w2+w3)
	   r12p=(eps2*w1-eps1*w2)/(eps2*w1+eps1*w2)
	   r23p=(eps3*w2-eps2*w3)/(eps3*w2+eps2*w3)
! transmission interface 21
	   t21s=2.d0*w2/(w2+w1)
	   t21p=2.d0*n2*n1*w2/(eps2*w1+eps1*w2)
! bilan des transmissions
	   q2=cdexp(2.d0*cim*w2*d)
	   t1s=t21s/(1.d0+r12s*r23s*q2)
	   t2s=t1s*r23s*q2
	   t1p=t21p/(1.d0+r12p*r23p*q2)
	   t2p=t1p*r23p*q2
!coeff des ondes planes
           coeff=cdexp(cim*w2*z0)
	   q1=t1p/coeff-t2p*coeff
	   q2=t1p/coeff+t2p*coeff
	   m1=t1s/coeff+t2s*coeff
           coeff=cdexp(cim*w1*z)/eps2
! propagateur electrique
!1ere ligne
	   fs(1)=k22*ku*m1*(sip*sip*j0+co2p*j10)/w2
	   fp(1)=cn21*w1*ku*q1*(cop*cop*j0-co2p*j10)
	   fs(2)=-k22*ku*m1*sip*cop*(j0-2.d0*j10)/w2
	   fp(2)=cn21*w1*ku*q1*sip*cop*(j0-2.d0*j10)
	   fp(3)=-cim*cn21*w1*ku*ku*cop*j1*q2/w2
!2eme ligne
	   fs(5)=k22*ku*m1*(cop*cop*j0-co2p*j10)/w2
	   fp(5)=cn21*w1*ku*q1*(sip*sip*j0+co2p*j10)
	   fp(6)=-cim*cn21*w1*ku*ku*sip*j1*q2/w2
! 3eme ligne
	   fp(7)=-cim*cn21*ku*ku*cop*j1*q1
	   fp(8)=-cim*cn21*ku*ku*sip*j1*q1
	   fp(9)=cn21*ku*ku*ku*j0*q2/w2
! propagateur mixte
!1ere ligne
	   gs(1)=k2*ku*m1*w1*sip*cop*(j0-2.d0*j10)/w2
	   gp(1)=-k1*ku*q1*sip*cop*(j0-2.d0*j10)
	   gs(2)=-k2*ku*w1*m1*(cop*cop*j0-co2p*j10)/w2
	   gp(2)=-k1*ku*q1*(sip*sip*j0+co2p*j10)
	   gp(3)=cim*k1*ku*ku*q2*sip*j1/w2
!2eme ligne
	   gs(4)=k2*ku*w1*m1*(sip*sip*j0+co2p*j10)/w2
	   gp(4)=k1*ku*q1*(cop*cop*j0-co2p*j10)
	   gp(6)=-cim*k1*ku*ku*q2*cop*j1/w2
! 3eme ligne
	   gs(7)=-cim*k2*ku*ku*m1*sip*j1/w2
	   gs(8)=cim*k2*ku*ku*m1*cop*j1/w2
! reconstruction
	   do l=1,9
	      f21r(l)=(fs(l)+fp(l))*coeff*cim
	      g21r(l)=(gs(l)+gp(l))*coeff*cim*n2
	   enddo
	endif
	RETURN
	END

