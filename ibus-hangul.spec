%define require_ibus_version 1.3.0
%define require_libhangul_version 0.0.10

Name:       ibus-hangul
Version:    1.3.0.20100329
Release:    1%{?dist}
Summary:    The Hangul engine for IBus input platform
License:    GPLv2+
Group:      System Environment/Libraries
URL:        http://code.google.com/p/ibus/
Source0:    http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  libhangul-devel >= %{require_libhangul_version}
BuildRequires:  pkgconfig
BuildRequires:  ibus-devel >= %{require_ibus_version}

Requires:   ibus >= %{require_ibus_version}
Requires:   libhangul >= %{require_libhangul_version}

%description
The Hangul engine for IBus platform. It provides Korean input method from
libhangul.

%prep
%setup -q

%build
%configure --disable-static
# make -C po update-gmo
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libexecdir}/ibus-engine-hangul
%{_libexecdir}/ibus-setup-hangul
%{_datadir}/ibus-hangul
%{_datadir}/ibus/component/*

%changelog
* Tue Apr 06 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.3.0.20100329-1
- Update version to 1.3.0.20100329

* Thu Feb 04 2010 Peng Huang <shawn.p.huang@gmail.com> - 1.2.0.20100102-1
- Update version to 1.2.0.20100102
- Add ibus-hangul-phuang.patch for ibus-1.2.99

* Fri Dec 11 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20091031-1
- Update version to 1.2.0.20091031.
- Drop ibus-hangul-1.1.0.20090328-right-ctrl-hanja.patch and
  ibus-hangul-1.1.0.20090328-hanja-arrow-keys.patch temporarily, because
  patches conflict with 1.2.0.20091031, and the key configure will available
  in next release.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20090617-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090330-1
- Update version to 1.2.0.20090617.

* Sun Apr 12 2009 Warren Togami <wtogami@redhat.com> - 1.1.0.20090330-2
- Bug 493706: ibus-hangul Hanja arrow keys are wrong
- Bug 493509: ibus-hangul missing right Ctrl for Hanja button
  These fixes are not ideal, but they make it usable for Fedora 11.
  These must become configurable in a future version.

* Mon Mar 30 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090330-1
- Update version to 1.1.0.20090330.
- Fix bug 486056 - missing options for 2bul, 3bul and other Korean layouts
- Fix bug 487269 - missing Hanja Conversion

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0.20090211-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090211-1
- Update version to 1.1.0.20090211.

* Thu Feb 05 2009 Peng Huang <shawn.p.huang@gmail.com> - 1.1.0.20090205-1
- Update version to 1.1.0.20090205.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1.1.20081023-2
- Rebuild for Python 2.6

* Thu Oct 23 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20081023-1
- Update to 0.1.1.20081023.

* Mon Sep 09 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080901-1
- Update to 0.1.1.20080901.

* Fri Aug 08 2008 Peng Huang <shawn.p.huang@gmail.com> - 0.1.1.20080823-1
- The first version.
