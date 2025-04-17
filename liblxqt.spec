%define major 2
%define libname %mklibname lxqt
%define oldlibname %mklibname lxqt 1
%define devname %mklibname lxqt -d
%define scm %nil

Summary:	Libraries for the LXQt desktop
Name:		liblxqt
Version:	2.2.0
%if "%scm" != ""
Release:	0.%{scm}1
Source0:	%{name}-%{scm}.tar.xz
%else
Release:	1
Source0:	https://github.com/lxqt/liblxqt/releases/download/%{version}/liblxqt-%{version}.tar.xz
%endif
Patch0:		liblxqt-2.0.0-config.patch
License:	LGPLv2.1+
Group:		System/Libraries
Url:		https://lxqt.org/
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	cmake(lxqt2-build-tools)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(qt6xdg)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(PolkitQt6-1)
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
Requires:	%{name} = %{EVRD}
%rename %{oldlibname}

%description -n %{libname}
Libraries for the LXQt desktop.

%files -n %{libname}
%{_libdir}/liblxqt.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	cmake(lxqt2-build-tools)
Requires:	pkgconfig(glib-2.0)

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

%cmake -DLXQT_ETC_XDG_DIR="%{_sysconfdir}/xdg" -DPULL_TRANSLATIONS=NO -G Ninja

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

# We get configs from distro-release
rm %{buildroot}%{_datadir}/lxqt/power.conf
