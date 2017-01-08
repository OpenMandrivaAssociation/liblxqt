%define major 0
%define libname %mklibname lxqt %{major}
%define devname %mklibname lxqt -d
%define scm %nil

Summary:	Libraries for the LXQt desktop
Name:		liblxqt
Version:	0.11.1
%if "%scm" != ""
Release:	1.%scm.1
Source0:	%{name}-%{scm}.tar.xz
%else
Release:	11
Source0:	https://github.com/lxde/%{name}/archive/%{name}-%{version}.tar.xz
%endif
License:	LGPLv2.1+
Group:		System/Libraries
Url:		http://lxqt.org/
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	ninja
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(qt5xdg)
BuildRequires:	cmake(KF5WindowSystem)

%description
Libraries for the LXQt desktop.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for the LXQt desktop
Group:		System/Libraries
Conflicts:	%{mklibname lxqt-qt5 0} < 0.9.0
%rename		%{_lib}lxqt-qt5_0
%rename		%{name}

%description -n %{libname}
Libraries for the LXQt desktop.

%files -n %{libname}
%{_libdir}/liblxqt.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	cmake(lxqt-build-tools)
%rename		%{_lib}lxqt-qt5-devel

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%files -n %{devname}
%dir %{_datadir}/cmake/lxqt
%dir %{_datadir}/cmake/lxqt/modules
%dir %{_datadir}/cmake/lxqt/find-modules
%{_includedir}/*
%{_libdir}/liblxqt.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/lxqt/*.cmake
%{_datadir}/cmake/lxqt/modules/*
%{_datadir}/cmake/lxqt/find-modules/FindXdgUserDirs.cmake
#----------------------------------------------------------------------------

%prep
%if "%scm" != ""
%setup -q -n %{name}
%else
%setup -q
%endif

%cmake_qt5 -DLXQT_ETC_XDG_DIR="%{_sysconfdir}/xdg" -DPULL_TRANSLATIONS=NO -G Ninja

%build
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja -C build

%install
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja_install -C build
