Summary:	A python interface to constant database files (cdb)
Name:		python-cdb
Version:	0.34
Release:	14
License:	GPL
Group:		Development/Python
URL:		https://pilcrow.madison.wi.us/
Source0:	http://pilcrow.madison.wi.us/python-cdb/%{name}-%{version}.tar.gz
BuildRequires:	python-devel >= 2.0
Requires:	python >= 2.0
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
The python-cdb extension module is an adaptation of D. J.
Bernstein's constant database package (see 
http://cr.yp.to/cdb.html).

cdb files are mappings of keys to values, designed for wickedly
fast lookups and atomic updates.  This module mimics the normal
cdb utilities, cdb(get|dump|make), via convenient, high-level
Python objects.

%prep

%setup -q

%build

CFLAGS="%{optflags}" python setup.py build

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

python setup.py install \
    --root="%{buildroot}" \
    --record="INSTALLED_FILES"

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc ChangeLog README COPYING Example





%changelog
* Thu Sep 17 2009 Bogdano Arendartchuk <bogdano@mandriva.com> 0.34-13mdv2010.0
+ Revision: 444176
- new version 0.34

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.32-13mdv2010.0
+ Revision: 442053
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.32-12mdv2009.0
+ Revision: 259520
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.32-11mdv2009.0
+ Revision: 247390
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.32-9mdv2008.1
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Dec 12 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.32-9mdv2007.0
+ Revision: 96021
- Rebuild for new python
- Rebuild for new python
- import python-cdb-0.32-7mdk

* Sun Jan 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.32-7mdk
- rebuild

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.32-6mdk
- Rebuild for new python

* Sat Oct 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.32-5mdk
- rpmbuildupdated

