%define upstream_name    Text-ASCIITable
%define upstream_version 0.22
Name:       perl-%{upstream_name}
Version:	0.22
Release:	1

Summary:    Create a nice formatted table using ASCII characters
License:    Artistic/GPL
Group:      Development/Perl
Url:        https://metacpan.org/dist/Text-ASCIITable
Source0:	https://cpan.metacpan.org/authors/id/L/LU/LUNATIC/Text-ASCIITable-0.22.tar.gz

BuildRequires:  perl(Module::Build)
BuildArch:      noarch
Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Pretty nifty if you want to output dynamic text to your console or other
fixed-size-font displays, and at the same time it will display it in a nice
human-readable, or "cool" way.

%prep
%setup -q -n %{upstream_name}-%{version}

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


