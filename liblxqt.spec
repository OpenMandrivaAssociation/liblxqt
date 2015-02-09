%define major 0
%define libname %mklibname lxqt %{major}
%define devname %mklibname lxqt -d
%define scm %nil

Summary:	Libraries for the LXQt desktop
Name:		liblxqt
Version:	0.9.0
%if "%scm" != ""
Release:	0.%scm.1	
Source0:	%{name}-%{scm}.tar.xz
%else
Release:	1
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
License:	LGPLv2.1+
Group:		System/Libraries
Url:		http://lxqt.org/
BuildRequires:	cmake
BuildRequires:	qt5-devel
BuildRequires:	cmake(qt5xdg)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(KF5WindowSystem)

%description
Libraries for the LXQt desktop.

%files
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%dir %{_datadir}/lxqt/translations/liblxqt
%{_datadir}/lxqt/translations/liblxqt/*.qm

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for the LXQt desktop
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
%rename %{mklibname lxqt-qt5 0}

%description -n %{libname}
Libraries for the LXQt desktop

%files -n %{libname}
%{_libdir}/liblxqt.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
%rename %{mklibname lxqt-qt5 -d}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%files -n %{devname}
%dir %{_datadir}/cmake/lxqt
%dir %{_datadir}/cmake/lxqt/modules
%{_includedir}/*
%{_libdir}/liblxqt.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/lxqt/*.cmake
%{_datadir}/cmake/lxqt/modules/*
#----------------------------------------------------------------------------

%prep
%if "%scm" != ""
%setup -q -n %{name}
%else
%setup -q
%endif

%build
%cmake -DUSE_QT5=ON
%make

%install
%makeinstall_std -C build

