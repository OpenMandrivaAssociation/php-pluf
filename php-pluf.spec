%define name    php-pluf
%define version 0.1
%define release %mkrel 3

Summary:    PHP WebApp Framework
Name:       %{name}
Version:    %{version}
Release:    %{release}
License:    GPLv2
Group:      Development/PHP
Url:        http://www.pluf.org/
Source0:    http://projects.ceondo.com/p/pluf/source/download/master/pluf-master.zip
Requires(pre):  rpm-helper   
Requires:       mod_php
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Simple, elegant and easy for people used to Django but in PHP5 so easy
to deploy all over the world.

%prep
%setup -q -n pluf-master

%build


%install
rm -rf %buildroot
%__install -d -m 755 %{buildroot}%_defaultdocdir/%{name}
%__install -m 755 COPYING CONTRIBUTORS 
cp -aRf apps %{buildroot}%_defaultdocdir/%{name}
cp -aRf tests %{buildroot}%_defaultdocdir/%{name}

%__install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -aRf src/* %{buildroot}%{_datadir}/%{name}
# Remove developper script
rm %{buildroot}%{_datadir}/%{name}/makepot.sh

# remove .htaccess files
find %{buildroot}%{_datadir}/%{name} -name .htaccess -exec rm -f {} \;


%files
%defattr(0644,root,root,0755)
%doc COPYING CONTRIBUTORS apps tests
%{_datadir}/%{name}


