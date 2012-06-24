#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	List
%define		pnam	Utils
Summary:	List::Utils - additional list utilities
Summary(pl):	List::Utils - dodatkowe narz�dzia do obs�ugi list
Name:		perl-List-Utils
Version:	0.06
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	69b3392ef0d5933043655eb55bc7b52d
BuildRequires:	perl-devel >= 5.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You know the things that Graham said could be implemented in Perl in
the List::Util (part of Scalar::List::Util release) docs but didn't?
Well, here they are.

%description -l pl
Kojarzysz rzeczy, o kt�rych Graham napisa� w dokumentacji od
List::Util (cz�� pakietu Scalar::List::Util), �e mog�yby by�
zaimplementowane w Perlu, ale nie s�? C�, oto one.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
