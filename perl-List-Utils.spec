%include	/usr/lib/rpm/macros.perl
%define	pdir	List
%define	pnam	Utils
Summary:	%{pdir}::%{pnam} -- Additional list utilities.
Summary(pl):	%{pdir}::%{pnam} -- Dodatkowe narz�dzia do obs�ugi list.
Name:		perl-%{pdir}-%{pnam}
Version:	0.01
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You know the things that Graham said could be implemented in Perl in the
List::Util (part of Scalar::List::Util release) docs but didn't?  Well,
here they are.

%description -l pl
Kojarzysz rzeczy, o kt�rych Graham napisa� w dokumentacji od List::Util
(cz�� pakietu Scalar::List::Util), �e mog�yby by� zaimplementowane w
Perlu, ale nie s�?  C�, oto one.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
