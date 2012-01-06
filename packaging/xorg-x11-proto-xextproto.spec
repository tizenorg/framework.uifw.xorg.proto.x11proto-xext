
Name:       xorg-x11-proto-xextproto
Summary:    X.Org X11 Protocol xextproto
Version:    7.1.2
Release:    1
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/xextproto-%{version}.tar.gz
Provides:   xextproto
BuildRequires: pkgconfig(xorg-macros)

%description
Description: %{summary}



%prep
%setup -q -n xextproto-%{version}


%build
%reconfigure --prefix=/usr --mandir=%{_datadir}/man --infodir=%{_datadir}/info \
	--disable-shared \
	CFLAGS="-Wall -g -D_F_ENABLE_XI2_SENDEVENT_"
	

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}






%files
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/xextproto.pc
%{_includedir}/X11/extensions/*.h
%{_datadir}/doc/xextproto/*.xml


