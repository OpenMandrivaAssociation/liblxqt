%define major 0
%define libname %mklibname lxqt %{major}
%define devname %mklibname lxqt -d

Summary:	Libraries for the LXQt desktop
Name:		liblxqt
Version:	0.7.0
Release:	3
License:	LGPLv2.1+
Group:		System/Libraries
Url:		http://lxqt.org/
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(qtxdg)

%description
Libraries for the LXQt desktop.

%files
%{_datadir}/lxqt/

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for the LXQt desktop
Group:		System/Libraries
Requires:	%{name}

%description -n %{libname}
Libraries for the LXQt desktop

%files -n %{libname}
%{_libdir}/liblxqt.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/liblxqt.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/lxqt

#----------------------------------------------------------------------------

%prep
%setup -q -c %{name}-%{version}

%build
%cmake
%make

%install
%makeinstall_std -C build

