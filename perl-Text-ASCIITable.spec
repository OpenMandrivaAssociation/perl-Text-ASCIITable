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


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2010.0
+ Revision: 405605
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.18-5mdv2009.0
+ Revision: 258609
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.18-4mdv2009.0
+ Revision: 246599
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.18-2mdv2008.1
+ Revision: 140721
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-2mdv2008.0
+ Revision: 67082
- rebuild


* Mon Jul 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2007.0
- New version 0.18
- Module::Build-based build

* Fri Apr 28 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.17-2mdk
- Fix SPEC according to Perl Policy
    - Source URL
- use mkrel

* Wed Sep 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdk
- New release 0.17

* Fri Sep 23 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdk
- new version 
- rpmbuildupdate aware
- fix directory ownership
- spec cleanup
- make test in %%check

* Tue May 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.15-1mdk
- First Mandriva release

