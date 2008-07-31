%define module  Text-ASCIITable
%define name    perl-%{module}
%define version 0.18
%define release %mkrel 5

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Create a nice formatted table using ASCII characters
License:    Artistic/GPL
Group:      Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Text/%{module}-%{version}.tar.bz2
BuildRequires:  perl(Module::Build)
BuildArch:      noarch
Buildroot:      %{_tmppath}/%{name}-%{version}

%description
Pretty nifty if you want to output dynamic text to your console or other
fixed-size-font displays, and at the same time it will display it in a nice
human-readable, or "cool" way.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Text
%{_mandir}/*/*

%clean
rm -rf %{buildroot}

