%define major 1
%define libname %mklibname lxqt %{major}
%define devname %mklibname lxqt -d
%define scm %nil

Summary:	Libraries for the LXQt desktop
Name:		liblxqt
Version:	1.2.0
%if "%scm" != ""
Release:	1.%{scm}.1
Source0:	%{name}-%{scm}.tar.xz
%else
Release:	4
Source0:	https://github.com/lxqt/liblxqt/releases/download/%{version}/liblxqt-%{version}.tar.xz
%endif
#Patch0:		liblxqt-0.13.0-find-qtxdg.patch
License:	LGPLv2.1+
Group:		System/Libraries
Url:		http://lxqt.org/
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	ninja
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	cmake(lxqt-build-tools)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(qt5xdg)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(PolkitQt5-1)
Requires:	%{libname} = %{EVRD}

%description
Libraries for the LXQt desktop.

%files
%{_bindir}/lxqt-backlight_backend
%{_datadir}/lxqt
%{_datadir}/polkit-1/actions/org.lxqt.backlight.pkexec.policy

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for the LXQt desktop
Group:		System/Libraries
Conflicts:	%{mklibname lxqt-qt5 0} < 0.9.0
Requires:	%{name} = %{EVRD}
Obsoletes:	%{mklibname lxqt 0} < %{EVRD}
%rename		%{_lib}lxqt-qt5_0

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
Requires:	pkgconfig(glib-2.0)
%rename		%{_lib}lxqt-qt5-devel

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%files -n %{devname}
%dir %{_datadir}/cmake/lxqt
%{_includedir}/*
%{_libdir}/liblxqt.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/lxqt/*.cmake
#----------------------------------------------------------------------------

%prep
%if "%scm" != ""
%autosetup -p1 -n %{name}
%else
%autosetup -p1
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
