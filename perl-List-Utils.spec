%include	/usr/lib/rpm/macros.perl
%define		pdir	List
%define		pnam	Utils
Summary:	List::Utils - additional list utilities
Summary(pl):	List::Utils - dodatkowe narzêdzia do obs³ugi list
Name:		perl-List-Utils
Version:	0.01
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You know the things that Graham said could be implemented in Perl in
the List::Util (part of Scalar::List::Util release) docs but didn't?
Well, here they are.

%description -l pl
Kojarzysz rzeczy, o których Graham napisa³ w dokumentacji od
List::Util (czê¶æ pakietu Scalar::List::Util), ¿e mog³yby byæ
zaimplementowane w Perlu, ale nie s±? Có¿, oto one.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
#%%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
