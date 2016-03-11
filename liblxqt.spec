%define major 0
%define libname %mklibname lxqt %{major}
%define devname %mklibname lxqt -d
%define scm %nil

Summary:	Libraries for the LXQt desktop
Name:		liblxqt
Version:	0.10.0
%if "%scm" != ""
Release:	1.%scm.1	
Source0:	%{name}-%{scm}.tar.xz
%else
Release:	4
Source0:	https://github.com/lxde/%{name}/archive/%{version}.tar.gz
%endif
License:	LGPLv2.1+
Group:		System/Libraries
Url:		http://lxqt.org/
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(qt5xdg)
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
Conflicts:	%{mklibname lxqt-qt5 0} < 0.9.0
%rename		%{_lib}lxqt-qt5_0

%description -n %{libname}
Libraries for the LXQt desktop

%files -n %{libname}
%{_libdir}/liblxqt.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
%rename		%{_lib}lxqt-qt5-devel

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
%cmake -DLXQT_ETC_XDG_DIR="%{_sysconfdir}/xdg"
%make

%install
%makeinstall_std -C build

