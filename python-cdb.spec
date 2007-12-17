Summary:	A python interface to constant database files (cdb)
Name:		python-cdb
Version:	0.32
Release:	%mkrel 9
License:	GPL
Group:		Development/Python
URL:		http://pilcrow.madison.wi.us/
Source0:	http://pilcrow.madison.wi.us/python-cdb/%{name}-%{version}.tar.bz2
BuildRequires:	python-devel >= 2.0
Requires:	python >= 2.0

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



