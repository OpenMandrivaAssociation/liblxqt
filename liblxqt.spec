%define major 0
%define libname %mklibname lxqt-qt5 %{major}
%define devname %mklibname lxqt-qt5 -d
%define qt4libname %mklibname lxqt %{major}
%define qt4devname %mklibname lxqt -d
%define scm %nil

Summary:	Libraries for the LXQt desktop
Name:		liblxqt
Version:	0.8.0
%if "%scm" != ""
Release:	0.%scm.1	
Source0:	%{name}-%{scm}.tar.xz
%else
Release:	2
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

%description
Libraries for the LXQt desktop.

%files
%{_datadir}/lxqt-qt5/

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for the LXQt desktop
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
%rename %{qt4libname}

%description -n %{libname}
Libraries for the LXQt desktop

%files -n %{libname}
%{_libdir}/liblxqt-qt5.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
%rename %{qt4devname}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/liblxqt-qt5.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/lxqt-qt5

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

