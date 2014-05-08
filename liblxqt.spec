%define major 0
%define libname %mklibname lxqt %{major}
%define devname %mklibname lxqt -d

Name: liblxqt
Version: 0.7.0
Release: 1
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
Summary: Libraries for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(qtxdg)
BuildRequires: cmake
BuildRequires: qt4-devel
Requires: %{libname} = %{EVRD}

%description
Libraries for the LXQt desktop

%package -n %{libname}
Summary: Libraries for the LXQt desktop
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Libraries for the LXQt desktop

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q -c %{name}-%{version}
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_datadir}/lxqt

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/lxqt
