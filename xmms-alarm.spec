%define name    xmms-alarm
%define version 0.3.7
%define release %mkrel 1

%define __libtoolize /bin/true

Summary: An alarm plugin for XMMS
Name: %{name}
Version: %{version}
Release: %{release}
Group: Sound
Source: http://www.snika.uklinux.net/%{name}/%{name}-%{version}.tar.bz2
License: GPL
BuildRequires: xmms1-devel >= 1.2.0
BuildRoot: %{_tmppath}/%{name}-buildroot
Url: http://www.snika.uklinux.net/

%description
xmms-alarm is an alarm plugin to use with XMMS that fades up the volume in
the morning and wakes you up.

%prep

%setup -q

%build

%configure --libdir=/%{_libdir}/xmms/General

%make

%install
rm -rf $RPM_BUILD_ROOT

make libdir=$RPM_BUILD_ROOT%{_libdir}/xmms/General install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/xmms/General/*
%doc COPYING INSTALL README

