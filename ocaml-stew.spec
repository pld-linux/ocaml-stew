Summary:	A stew of OCaml utility function
Summary(pl):	Zbiór funkcji narzêdziowych dla OCamla
Name:		ocaml-stew
Version:	0.12.0
Release:	3
License:	LGPL
Group:		Libraries
Vendor:		Shawn Wagner <shawnw@speakeasy.org>
Source0:	http://raevnos.pennmush.org/code/stew-%{version}.tar.gz
# Source0-md5:	7e822ca90a5265a2f1b94e81add6eb4c
URL:		http://raevnos.pennmush.org/code/ocaml.html
BuildRequires:	autoconf
BuildRequires:	ocaml >= 3.07
BuildRequires:	ocaml-findlib >= 0.7.2
BuildRequires:	ocaml-pcre-devel
%requires_eq	ocaml-pcre
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Stew is a general-purpose library of useful utility and extension
routines. Highlights include random number generators and
distributions, locale support, improved time printing, and character
classification routines that are locale-dependant.

This package contains files needed to run bytecode executables using
this library.

%description -l pl
Stew jest ogólnego u¿ytku bibliotek± u¿ytecznych funkcji narzêdziowych
i rozszerzeñ. Zawiera generatory i dystrybucje liczb losowych,
wsparcie dla lokalizacji, ulepszone drukowanie czasu, oraz funkcje
klasyfikacji znaków (<ctype.h>), które s± zale¿ne od locale.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
u¿ywaj±cych tej biblioteki.

%package devel
Summary:	A stew of OCaml utility function - development part
Summary(pl):	Zbiór funkcji narzêdziowych dla OCamla - cze¶æ programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
Stew is a general-purpose library of useful utility and extension
routines. Highlights include random number generators and
distributions, locale support, improved time printing, and character
classification routines that are locale-dependant.

This package contains files needed to develop OCaml programs using
this library.

%description devel -l pl
Stew jest ogólnego u¿ytku bibliotek± u¿ytecznych funkcji narzêdziowych
i rozszerzeñ. Zawiera generatory i dystrybucje liczb losowych,
wsparcie dla lokalizacji, ulepszone drukowanie czasu, oraz funkcje
klasyfikacji znaków (<ctype.h>), które s± zale¿ne od locale.

Pakiet ten zawiera pliki niezbêdne do tworzenia programów u¿ywaj±cych
tej biblioteki.

%prep
%setup -q -n stew-%{version}

%build
%{__autoconf}
%configure
%{__make} all opt
rm -f *.cma
%{__make} DLL='-cclib -lstew'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/{stublibs,site-lib/stew}

ln -s ../stublibs $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib

%{__make} install \
	CAMLLIB=$RPM_BUILD_ROOT%{_libdir}/ocaml \
	OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml

echo >> $RPM_BUILD_ROOT%{_libdir}/ocaml/stew/META
echo 'directory = "+stew"' >> $RPM_BUILD_ROOT%{_libdir}/ocaml/stew/META
mv -f $RPM_BUILD_ROOT%{_libdir}/ocaml/stew/META \
	$RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/stew
rm -f $RPM_BUILD_ROOT%{_libdir}/ocaml/stew/*.mli

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/ocaml/stublibs/*.so

%files devel
%defattr(644,root,root,755)
%doc html/*
%{_libdir}/ocaml/stew
%{_libdir}/ocaml/site-lib/stew
