Name:           leechcraft 
Summary:        A free open source cross-platform modular internet-client 
Version:        0.4.75
Release:        0.1.gitga29292b%{?dist}
License:        GPLv2+
Group:          Applications/Internet
Url:            http://leechcraft.org
Source:         http://netcologne.dl.sourceforge.net/project/leechcraft/LeechCraft/snapshots/leechcraft-0.4.75-285-ga29292b.tar.bz2
Source1:        %{name}.desktop

Requires:       %{name}-iconset
Requires:       %{name}-devel

BuildRequires:  cmake
BuildRequires:  libcurl-devel
BuildRequires:  phonon-devel
BuildRequires:  openssl-devel
BuildRequires:  boost-devel 
BuildRequires:  qt4-devel
BuildRequires:  qt-webkit-devel
BuildRequires:  qjson-devel
BuildRequires:  qscintilla-devel
BuildRequires:  GeoIP-devel 
BuildRequires:  bzip2-devel
BuildRequires:  qxmpp >= 0.3.44
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  rb_libtorrent-devel >= 0.15.6
BuildRequires:  gettext-devel


%description
Core executable of Leechcraft
LeechCraft is a free modular "Internet client" application.

LeechCraft allows to browse the web, read RSS/Atom feeds, download
files via BitTorrent, HTTP, FTP and DC, automatically stream,
download or play podcasts and other media files and much more.

Features can be easily added via plugins that can be integrated with
each other with no effert while staying abstract from the exact
implementation.

This package contains the main LeechCraft executable, which connects
all the plugins with each other, routes requests between them, tracks
dependencies and performs several other housekeeping tasks.

%package devel
Summary:    Leechcraft
Requires:   %{name} = %{version}
Group:      Development/Libraries

%description devel
This package contains header files required to develop new modules for
LeechCraft.

%package aggregator
Summary:        LeechCraft Aggregator Module
Requires:       %{name} = %{version}
 
%description aggregator
RSS/Atom feed reader for LeechCraft.
 
This package contains Aggregator, the RSS/Atom feed reader. It features:
 * RSS 0.92/0.93/1.0/2.0, Atom 0.3/1.0;
 * extensions like GeoRSS, MediaRSS, Comment API etc;
 * OPML support;
 * broadcatching and fetching arbitrary data with regexps;
 * tape mode for news display;
 * individual options for each channel like update interval;
 * storage either in SQLite or PostgreSQL;
 * exporting feeds to FB2 for further reading on handheld devices.

A web browser plugin is recommended to show the news in a fancy way.
 
%package auscrie
Summary:        LeechCraft Auscrie Module
Requires:       %{name} = %{version}
 
%description auscrie
Screenshooter for LeechCraft.
 
This package contains Auscrie, an auto screenshooter for LeechCraft.
It can make screenshots of LeechCraft and then either save them locally
or upload them to an imagebin.
 
%package popishu
Summary:        Leechcraft Popishu Module
Requires:       %{name} = %{version}
Requires:       qscintilla

%description popishu
Popishu is a text editor for Leechcraft.
 
%package cstp
Summary:        LeechCraft HTTP Module
Requires:       %{name} = %{version}
 
%description cstp
HTTP client for LeechCraft.
 
This package contains clean and simple HTTP implementation.
 
%package dbusmanager
Summary:        Leechcraft D-Bus Module
Requires:       %{name} = %{version}
 
%description dbusmanager
D-Bus side of LeechCraft.
 
This package provides some DBus-related features, like integration with
desktop notifications (KDE ≥ 4.4 and others supporting libnotify
interfaces).
 
%package deadlyrics
Summary:        LeechCraft Lyrics Module
Requires:       %{name} = %{version}
 
%description deadlyrics
Song lyrics finder for LeechCraft.
 
This package contains a simple client for finding song lyrics on various
sites.
 
%package historyholder
Summary:        LeechCraft History Module
Requires:       %{name} = %{version}

%description historyholder
History keeper for LeechCraft.
 
This package contains a history keeper that stores information about
finished downloads and similar events.
 
%package kinotify
Summary:        LeechCraft Kinotify Module
Requires:       %{name} = %{version}
 
%description kinotify
Fancy notifications for LeechCraft.
 
This package contains Kinotify which provides fancy notifications for
LeechCraft instead of old-style tray-based ones.
 
%package lmp
Summary:        LeechCraft LMP Module
Requires:       %{name} = %{version}
 
%description lmp
Media previewer for LeechCraft.
 
This package contains the LMP, LeechCraft Media Previewer, small and
dirty media player designed to preview already downloaded files or to
stream media content live.
 
%package lcftp
Summary:        LeechCraft FTP Module
Requires:       %{name} = %{version}
 
%description lcftp
FTP client for LeechCraft.
 
This package adds FTP support and provides a simple two-panel FTP
client based on libcurl.
 
%package networkmonitor
Summary:        LeechCraft Network Monitor Module
Requires:       %{name} = %{version}
 
%description networkmonitor
Network monitor for LeechCraft.
 
This package contains a monitor that watches for HTTP requests
and responses around.
 
%package newlife
Summary:        LeechCraft Importer Module
Requires:       %{name} = %{version}
 
%description newlife
Settings importer for LeechCraft.
 
This package contains importer of settings, preferences etc. from
various applications into LeechCraft. Currently it supports importing
RSS feeds and settings from Akregator and Liferea.
 
%package poshuku
Summary:        LeechCraft Web Browser Module
Requires:       %{name} = %{version}
 
%description poshuku
Web browser for LeechCraft.
 
This package contains a full-featured web browser for LeechCraft based
on WebKit. Poshuku is fully extensible with plugins. Currently it
features:
 * support for all major web-standards;
 * integration with other plugins;
 * autodiscovery;
 * tagging bookmarks;
 * support for SQLite or PostgreSQL storage.
 
%package poshuku-fatape
Summary:        LeechCraft Greasemonkey Module
Requires:       %{name} = %{version}
Requires:       %{name}-poshuku
 
%description poshuku-fatape
Greasemonkey scripts for leechcraft-poshuku.
 
%package poshuku-cleanweb
Summary:        LeechCraft Ad Filter Module
Requires:       %{name} = %{version}
Requires:       %{name}-poshuku
 
%description poshuku-cleanweb
Ad filter for Web browser for LeechCraft.
 
This package contains a plugin for the Poshuku web browser that
filters out ads according to predefined rules. It is compatible with
Firefox's AdBlock rules list files. It also supports disabling Flash
and allowing it to load only after you click on the corresponding
button.
 
%package poshuku-filescheme
Summary:        LeechCraft Schemes Module
Requires:       %{name} = %{version}
Requires:       %{name}-poshuku = %{version}
 
%description poshuku-filescheme
file://-schemes support for a Web browser for LeechCraft.
 
This package contains a plugin for the Poshuku web browser that allows
it to handle file:// schemes.
 
%package poshuku-fua
Summary:        LeechCraft User Agent Module
Requires:       %{name} = %{version}
Requires:       %{name}-poshuku = %{version}
 
%description poshuku-fua
Fake user agent plugin for Web browser for LeechCraft.
 
This package contains a plugin for the Poshuku web browser that allows
it to set fake user agents for different domains or even URLs based on
regexps.
 
%package poshuku-wyfv
Summary:        LeechCraft Flash Video Replacer Module
Requires:       %{name} = %{version}
Requires:       %{name}-poshuku = %{version}
 
%description poshuku-wyfv
Flash video replacer for Web browser for LeechCraft.
 
This package contains a plugin for the Poshuku web browser that
replaces default flash-based video players on some sites with any
suitable LeechCraft's media player thus avoiding the need for Flash.


%package poshuku-pintab
Summary:        LeechCraft Pintab Module
Requires:       %{name} = %{version}
Requires:       %{name}-poshuku = %{version}
 
%description poshuku-pintab
Poshuku PinTab allows to pin selected Poshuku tabs so that they cannot be closed until unpinned.

%package poshuku-onlinebookmarks
Summary:        LeechCraft Online Bookmarks Module
Requires:       %{name} = %{version}
Requires:       %{name}-poshuku = %{version}
 
%description poshuku-onlinebookmarks
Online bookmarks plugin for LeechCraft.
 
This package contains a plugin for the Poshuku web browser that allows
to synchronize bookmarks with services like Read It Later.
 
%package seekthru
Summary:        LeechCraft OpenSearch Module
Requires:       %{name} = %{version}
 
%description seekthru
OpenSearch-support plugin for LeechCraft.
 
This package contains a search client for OpenSearch-aware web sites.
 
%package summary
Summary:        LeechCraft Summary Module
Requires:       %{name} = %{version}
 
%description summary
Quick summary of what's going on in LeechCraft.
 
This package contains Summary which shows currently running download
tasks like BitTorrent files as well as news, events and statuses, like
unread items in RSS feed reader. It also allows to perform search
queries with instaled search plugins.
 
%package tabpp
Summary:        LeechCraft Tab++ Module
Requires:       %{name} = %{version}
 
%description tabpp
Tabbing experience enhancer for LeechCraft.
 
This package contains Tab++ which shows the tree of tabs in groups. For
example, tabs with pages in a browser that belong to the same subdomain
will be grouped, and subdomains of the same parent domain will become
its children as well.
 
%package vgrabber
Summary:        LeechCraft Vkontakte Module
Requires:       %{name} = %{version}
 
%description vgrabber
Vkontakte.ru plugin for LeechCraft.
 
This package contains a music search/grabber for the vkontakte.ru social
network.
 
%package shellopen
Summary:        Leechcraft Shellopen Module
Requires:       %{name} = %{version}
 
%description shellopen
Support for opening files with external apps in LeechCraft.
 
This package contains module that adds an option to open files and
handle entities with external applications. For example, you may choose
to open a video file with your favorite media player instead of LC's
one.
 
%package secman
Summary:        LeechCraft Security Manager Module
Requires:       %{name} = %{version}
 
%description secman
Security manager for LeechCraft.
 
This package contains the base plugin for secure storage and such
stuff for LeechCraft. Particular storage backends are implemented
by plugins for this plugin.
 
%package secman-simplestorage
Summary:        LeechCraft Simple Storage Module
Requires:       %{name} = %{version}
 
%description secman-simplestorage
Simple storage backend for SecMan.
 
This package contains a simple, unencrypted storage backend for
SecMan, LeechCraft's security manager plugin.
 
%package azoth
Summary:        LeechCraft Messenger Module
Requires:       %{name} = %{version}
Requires:       qxmpp >= 0.3.44

%description azoth
XMPP, IRC messenger for LeechCraft.
 
This package contains a simple XMPP messenger for LeechCraft.
 
%package iconset-oxygen
Summary:        LeechCraft Oxygen Iconset
Requires:       %{name} = %{version}
Requires:       oxygen-icon-theme
Provides:       %{name}-iconset
BuildArch:      noarch
 
%description iconset-oxygen
Oxygen-based iconset for LeechCraft.
 
This package contains icons taken from the Oxygen project for LeechCraft.
 
%package iconset-tango
Summary:        Leechcraft
Requires:       %{name} = %{version}
Requires:       tango-icon-theme
Provides:       %{name}-iconset
BuildArch:      noarch
 
%description iconset-tango
Iconset based on the Tango project for LeechCraft.
 
This package contains mapping to the Tango project icons.
 
%package bittorrent
Summary:    BitTorrent, the BitTorrent client
Requires:   %{name} = %{version}
Requires:   rb_libtorrent-devel >= 0.15.6

%description bittorrent
BitTorrent, the BitTorrent client for LeechCraft.

%package eiskaltdcpp
Summary:        LeechCraft DC++ Module
Requires:       %{name} = %{version}

%description eiskaltdcpp
DC++ client for LeechCraft.

This package contains EiskaltDC++ DirectConnect client ported to
LeechCraft.

%package advancednotifications
Summary:        LeechCraft DC++ Module
Requires:       %{name} = %{version}

%description advancednotifications
Advanced Notifications module for more customizable notifications for Leechcraft

%prep
%setup -q -n %{name}-%{version}-285-ga29292b

mkdir build 

%build
cd build

%{cmake} \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DLEECHCRAFT_VERSION="0.4.75" \
  -DENABLE_TORRENT=True \
  -DRESPECTLIB64=True \
  -DENABLE_SECMAN=True \
  -DENABLE_POPISHU=True \
  -DENABLE_AZOTH=True \
  -DENABLE_EISKALTDCPP=True \
  -DENABLE_ADVANCEDNOTIFICATIONS=True \
  ../src  

make %{?_smp_mflags}

%install
cd build
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install                                    \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
  %{SOURCE1}

%post
/sbin/ldconfig
 
%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README COPYING
%_bindir/%{name}
%_bindir/%{name}-add-file
%_datadir/%{name}/settings/coresettings.xml
%doc %_datadir/man/man1/%{name}.1.gz
%_datadir/applications/%{name}.desktop
%_datadir/icons/hicolor/*/*/*
%_datadir/icons/Pevzi
%dir %_datadir/%{name}/icons
%dir %_libdir/%{name}
%dir %_libdir/%{name}/plugins
%dir %_datadir/%{name}
%dir %_datadir/%{name}/settings
%dir %_datadir/%{name}/translations
%_datadir/%{name}/icons/Pevzi.mapping
%dir %_datadir/%{name}/installed
%_datadir/%{name}/translations/leechcraft_??.qm
%_datadir/%{name}/translations/leechcraft_??_??.qm
%_libdir/*plugininterface.so.*
%_libdir/*xmlsettingsdialog.so.*

%files  bittorrent
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_bittorrent.so
%{_datadir}/%{name}/settings/torrentsettings.xml
%{_datadir}/%{name}/translations/%{name}_bittorrent_*.qm

%files  eiskaltdcpp
%defattr(-,root,root)
%{_datadir}/%{name}/eiskaltdcpp
%dir %{_datadir}/%{name}/translations/??
%dir %{_datadir}/%{name}/translations/??/LC_MESSAGES
%lang(be) %{_datadir}/%{name}/translations/be/LC_MESSAGES/libeiskaltdcpp.mo
%lang(bg) %{_datadir}/%{name}/translations/bg/LC_MESSAGES/libeiskaltdcpp.mo
%lang(cs) %{_datadir}/%{name}/translations/cs/LC_MESSAGES/libeiskaltdcpp.mo
%lang(en) %{_datadir}/%{name}/translations/en/LC_MESSAGES/libeiskaltdcpp.mo
%lang(es) %{_datadir}/%{name}/translations/es/LC_MESSAGES/libeiskaltdcpp.mo
%lang(fr) %{_datadir}/%{name}/translations/fr/LC_MESSAGES/libeiskaltdcpp.mo
%lang(hu) %{_datadir}/%{name}/translations/hu/LC_MESSAGES/libeiskaltdcpp.mo
%lang(pl) %{_datadir}/%{name}/translations/pl/LC_MESSAGES/libeiskaltdcpp.mo
%lang(ru) %{_datadir}/%{name}/translations/ru/LC_MESSAGES/libeiskaltdcpp.mo
%lang(sk) %{_datadir}/%{name}/translations/sk/LC_MESSAGES/libeiskaltdcpp.mo
%lang(sr) %{_datadir}/%{name}/translations/sr/LC_MESSAGES/libeiskaltdcpp.mo
%lang(uk) %{_datadir}/%{name}/translations/uk/LC_MESSAGES/libeiskaltdcpp.mo
%{_libdir}/%{name}/plugins/*%{name}_eiskaltdcpp.so
%doc %{_mandir}/man1/eiskaltdcpp-qt.1.gz

%files poshuku-pintab
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*_poshuku_pintab.so

%files aggregator
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_aggregator.so
%_datadir/%{name}/translations/%{name}_aggregator*.qm
%_datadir/%{name}/settings/aggregatorsettings.xml

%files auscrie
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/lib%{name}_auscrie.so
%_datadir/%{name}/translations/%{name}_auscrie_*.qm

%files azoth
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_azoth*.so
%_datadir/%{name}/translations/%{name}_azoth*.qm
%_datadir/%{name}/settings/azoth*.xml
%_datadir/%{name}/azoth/

%files cstp
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*leechcraft_cstp.so
%_datadir/%{name}/translations/leechcraft_cstp*.qm
%_datadir/%{name}/settings/cstpsettings.xml

%files dbusmanager
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*leechcraft_dbusmanager.so
%_datadir/%{name}/translations/leechcraft_dbusmanager*.qm
%_datadir/%{name}/settings/dbusmanagersettings.xml

%files deadlyrics
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_deadlyrics.so
%_datadir/%{name}/translations/%{name}_deadlyrics*.qm
%_datadir/%{name}/settings/deadlyricssettings.xml

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}/
%_datadir/%{name}/cmake
%_libdir/*plugininterface.so
%_libdir/*xmlsettingsdialog.so

%files historyholder
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*leechcraft_historyholder.so
%_datadir/%{name}/translations/leechcraft_historyholder*.qm

%files iconset-oxygen
%defattr(-,root,root,-)
%_datadir/icons/oxygen/
%_datadir/%{name}/icons/oxygen.mapping

%files iconset-tango
%defattr(-,root,root,-)
%_datadir/%{name}/icons/Tango.mapping

%files kinotify
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_kinotify.so
%_datadir/%{name}/kinotify/
%_datadir/%{name}/settings/kinotifysettings.xml

%files lcftp
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_lcftp.so
%_datadir/%{name}/translations/%{name}_lcftp*.qm
%_datadir/%{name}/settings/lcftpsettings.xml

%files lmp
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_lmp.so
%_datadir/%{name}/translations/%{name}_lmp*
%_datadir/%{name}/settings/lmpsettings.xml

%files networkmonitor
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_networkmonitor.so
%_datadir/%{name}/translations/%{name}_networkmonitor*.qm

%files newlife
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_newlife.so
%_datadir/%{name}/translations/%{name}_newlife*.qm

%files poshuku-cleanweb
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_poshuku_cleanweb.so
%_datadir/%{name}/translations/%{name}_poshuku_cleanweb*.qm
%_datadir/%{name}/settings/poshukucleanwebsettings.xml

%files poshuku-filescheme
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_poshuku_filescheme.so
%_datadir/%{name}/translations/%{name}_poshuku_filescheme_*.qm

%files poshuku-fua
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_poshuku_fua.so
%_datadir/%{name}/translations/%{name}_poshuku_fua*.qm
%_datadir/%{name}/settings/poshukufuasettings.xml

%files popishu
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_popishu.so
%_datadir/%{name}/translations/%{name}_popishu_*.qm
%_datadir/%{name}/settings/popishusettings.xml

%files poshuku
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_poshuku.so
%_datadir/%{name}/settings/poshukusettings.xml
%_datadir/%{name}/installed/poshuku/
%_datadir/%{name}/translations/%{name}_poshuku_??.qm
%_datadir/%{name}/translations/%{name}_poshuku_??_??.qm

%files poshuku-fatape
%defattr(-,root,root,-)
%_datadir/%{name}/settings/poshukufatapesettings.xml
%_libdir/%{name}/plugins/*%{name}_poshuku_fatape.so
%_datadir/%{name}/translations/leechcraft_poshuku_fatape*

%files poshuku-wyfv
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_poshuku_wyfv.so
%_datadir/%{name}/translations/%{name}_poshuku_wyfv*.qm
%_datadir/%{name}/settings/poshukuwyfvsettings.xml

%files poshuku-onlinebookmarks
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_poshuku_onlinebookmarks.so
%_datadir/%{name}/settings/poshukuonlinebookmarkssettings.xml
%_datadir/%{name}/translations/%{name}_poshuku_onlinebookmarks*.qm

%files secman
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_secman.so

%files secman-simplestorage
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_secman_simplestorage.so

%files seekthru
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_seekthru.so
%_datadir/%{name}/translations/%{name}_seekthru*.qm
%_datadir/%{name}/settings/seekthrusettings.xml

%files shellopen
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_shellopen.so
%_datadir/%{name}/translations/%{name}_shellopen*.qm

%files summary
%defattr(-,root,root,-) 
%_libdir/%{name}/plugins/*%{name}_summary.so 
%_datadir/%{name}/translations/%{name}_summary*.qm

%files tabpp
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_tabpp.so
%_datadir/%{name}/translations/%{name}_tabpp_*.qm
%_datadir/%{name}/settings/tabppsettings.xml

%files vgrabber
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*%{name}_vgrabber.so
%_datadir/%{name}/translations/%{name}_vgrabber*.qm
%_datadir/%{name}/settings/vgrabbersettings.xml

%files advancednotifications
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/*%{name}_advancednotifications.so

%changelog
* Mon Jun 06 2011 Minh Ngo <nlminhtl@gmail.com> - 0.4.75-0.1.gitga29292b
- initial build 
