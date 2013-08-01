Summary: OpenAL Soft
Name: OpenAL
Version: 1.15.1
Release: 2
Source: %{name}-%{version}.tar.bz2
URL: http://kcat.strangesoft.net/openal.html
License: LGPL
Group: Development/Libraries
BuildRequires: cmake
BuildRequires: pkgconfig(libpulse)


%description
OpenAL provides capabilities for playing audio in a virtual 3D environment.
Distance attenuation, doppler shift, and directional sound emitters are among
the features handled by the API. More advanced effects, including air
absorption, occlusion, and environmental reverb, are available through the EFX
extension. It also facilitates streaming audio, multi-channel buffers, and
audio capture.

%package devel
Summary: OpenAL Soft - Development libraries
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
OpenAL provides capabilities for playing audio in a virtual 3D environment.
Distance attenuation, doppler shift, and directional sound emitters are among
the features handled by the API. More advanced effects, including air
absorption, occlusion, and environmental reverb, are available through the EFX
extension. It also facilitates streaming audio, multi-channel buffers, and
audio capture.


%prep
%setup -q 

%build
%cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .
make

%install
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README COPYING env-vars.txt hrtf.txt
%{_libdir}/lib*.so.*
%{_datadir}/openal/*

%files devel
%defattr(-,root,root,-)
%doc README COPYING env-vars.txt hrtf.txt
%{_bindir}/*
%{_libdir}/lib*.so
%{_includedir}/*/*.h
%{_libdir}/pkgconfig/*

