#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-WWW-Form-UrlEncoded-XS
Version  : 0.28
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/WWW-Form-UrlEncoded-XS-0.28.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/WWW-Form-UrlEncoded-XS-0.28.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libw/libwww-form-urlencoded-xs-perl/libwww-form-urlencoded-xs-perl_0.25-1.debian.tar.xz
Summary  : 'XS implementation of parser and builder for application/x-www-form-urlencoded'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-WWW-Form-UrlEncoded-XS-license = %{version}-%{release}
Requires: perl-WWW-Form-UrlEncoded-XS-perl = %{version}-%{release}
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
Provides: perl-WWW-Form-UrlEncoded-XS-devel = %{version}-%{release}
Requires: perl-WWW-Form-UrlEncoded-XS = %{version}-%{release}

%description dev
dev components for the perl-WWW-Form-UrlEncoded-XS package.


%package license
Summary: license components for the perl-WWW-Form-UrlEncoded-XS package.
Group: Default

%description license
license components for the perl-WWW-Form-UrlEncoded-XS package.


%package perl
Summary: perl components for the perl-WWW-Form-UrlEncoded-XS package.
Group: Default
Requires: perl-WWW-Form-UrlEncoded-XS = %{version}-%{release}

%description perl
perl components for the perl-WWW-Form-UrlEncoded-XS package.


%prep
%setup -q -n WWW-Form-UrlEncoded-XS-0.28
cd %{_builddir}
tar xf %{_sourcedir}/libwww-form-urlencoded-xs-perl_0.25-1.debian.tar.xz
cd %{_builddir}/WWW-Form-UrlEncoded-XS-0.28
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/WWW-Form-UrlEncoded-XS-0.28/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
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
cp %{_builddir}/WWW-Form-UrlEncoded-XS-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-WWW-Form-UrlEncoded-XS/220fe941787679d8a043c0444548ac186c86f309 || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-WWW-Form-UrlEncoded-XS/6a1f9ee5ecd3e725a7167826a7eee8a2ec733b06 || :
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/WWW::Form::UrlEncoded::XS.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-WWW-Form-UrlEncoded-XS/220fe941787679d8a043c0444548ac186c86f309
/usr/share/package-licenses/perl-WWW-Form-UrlEncoded-XS/6a1f9ee5ecd3e725a7167826a7eee8a2ec733b06

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
