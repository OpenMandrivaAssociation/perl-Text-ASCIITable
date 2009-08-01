%define upstream_name    Text-ASCIITable
%define upstream_version 0.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Create a nice formatted table using ASCII characters
License:    Artistic/GPL
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(Module::Build)
BuildArch:      noarch
Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Pretty nifty if you want to output dynamic text to your console or other
fixed-size-font displays, and at the same time it will display it in a nice
human-readable, or "cool" way.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
