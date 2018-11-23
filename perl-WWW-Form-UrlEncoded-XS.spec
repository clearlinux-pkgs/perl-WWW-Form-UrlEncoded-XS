#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-WWW-Form-UrlEncoded-XS
Version  : 0.25
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/WWW-Form-UrlEncoded-XS-0.25.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/WWW-Form-UrlEncoded-XS-0.25.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libw/libwww-form-urlencoded-xs-perl/libwww-form-urlencoded-xs-perl_0.25-1.debian.tar.xz
Summary  : 'XS implementation of parser and builder for application/x-www-form-urlencoded'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-WWW-Form-UrlEncoded-XS-lib = %{version}-%{release}
Requires: perl-WWW-Form-UrlEncoded-XS-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)

%description
[![Build Status](https://travis-ci.org/kazeburo/WWW-Form-UrlEncoded-XS.svg?branch=master)](https://travis-ci.org/kazeburo/WWW-Form-UrlEncoded-XS)
# NAME

%package dev
Summary: dev components for the perl-WWW-Form-UrlEncoded-XS package.
Group: Development
Requires: perl-WWW-Form-UrlEncoded-XS-lib = %{version}-%{release}
Provides: perl-WWW-Form-UrlEncoded-XS-devel = %{version}-%{release}

%description dev
dev components for the perl-WWW-Form-UrlEncoded-XS package.


%package lib
Summary: lib components for the perl-WWW-Form-UrlEncoded-XS package.
Group: Libraries
Requires: perl-WWW-Form-UrlEncoded-XS-license = %{version}-%{release}

%description lib
lib components for the perl-WWW-Form-UrlEncoded-XS package.


%package license
Summary: license components for the perl-WWW-Form-UrlEncoded-XS package.
Group: Default

%description license
license components for the perl-WWW-Form-UrlEncoded-XS package.


%prep
%setup -q -n WWW-Form-UrlEncoded-XS-0.25
cd ..
%setup -q -T -D -n WWW-Form-UrlEncoded-XS-0.25 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/WWW-Form-UrlEncoded-XS-0.25/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-WWW-Form-UrlEncoded-XS
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-WWW-Form-UrlEncoded-XS/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-WWW-Form-UrlEncoded-XS/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/WWW/Form/UrlEncoded/XS.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/WWW::Form::UrlEncoded::XS.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/auto/WWW/Form/UrlEncoded/XS/XS.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-WWW-Form-UrlEncoded-XS/LICENSE
/usr/share/package-licenses/perl-WWW-Form-UrlEncoded-XS/deblicense_copyright
