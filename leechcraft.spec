Name:           leechcraft 
Summary:        A free open source cross-platform modular internet-client 
Version:        0.4.85
Release:        0.1%{?dist}.R
License:        GPLv2+
Group:          Applications/Internet
Url:            http://leechcraft.org
Source:         http://netcologne.dl.sourceforge.net/project/%{name}/LeechCraft/%{version}/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop

Requires:       %{name}-iconset

BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  boost-devel 
BuildRequires:  qt4-devel
BuildRequires:  qt-webkit-devel
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  oxygen-icon-theme
BuildRequires:  gettext-devel

#LCFTP
BuildRequires:  libcurl-devel

#Poshuku dependencies
BuildRequires:  qjson-devel

#LMP dependencies
BuildRequires:  phonon-devel

#Popishu dependencies
BuildRequires:  qscintilla-devel

#BitTorrent dependencies
%if 0%{?fedora} >= 15
BuildRequires:  rb_libtorrent-devel >= 0.15.6
%endif

#Azoth dependencies
BuildRequires:  aspell-devel
BuildRequires:  speex-devel
BuildRequires:  qxmpp >= 0.3.45.1
BuildRequires:  GeoIP-devel 
BuildRequires:  qca2-devel

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
Requires:       %{name}-cstp = %{version}
 
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
Requires:       %{name}-poshuku = %{version}
 
%description poshuku-fatape
Greasemonkey scripts for leechcraft-poshuku.
 
%package poshuku-cleanweb
Summary:        LeechCraft Ad Filter Module
Requires:       %{name}-poshuku = %{version}
 
%description poshuku-cleanweb
Ad filter for Web browser for LeechCraft.
 
This package contains a plugin for the Poshuku web browser that
filters out ads according to predefined rules. It is compatible with
Firefox's AdBlock rules list files. It also supports disabling Flash
and allowing it to load only after you click on the corresponding
button.
 
%package poshuku-filescheme
Summary:        LeechCraft Schemes Module
Requires:       %{name}-poshuku = %{version}
 
%description poshuku-filescheme
file://-schemes support for a Web browser for LeechCraft.
 
This package contains a plugin for the Poshuku web browser that allows
it to handle file:// schemes.
 
%package poshuku-fua
Summary:        LeechCraft User Agent Module
Requires:       %{name}-poshuku = %{version}
 
%description poshuku-fua
Fake user agent plugin for Web browser for LeechCraft.
 
This package contains a plugin for the Poshuku web browser that allows
it to set fake user agents for different domains or even URLs based on
regexps.
 
%package poshuku-wyfv
Summary:        LeechCraft Flash Video Replacer Module
Requires:       %{name}-poshuku = %{version}
 
%description poshuku-wyfv
Flash video replacer for Web browser for LeechCraft.
 
This package contains a plugin for the Poshuku web browser that
replaces default flash-based video players on some sites with any
suitable LeechCraft's media player thus avoiding the need for Flash.


%package poshuku-pintab
Summary:        LeechCraft Pintab Module
Requires:       %{name}-poshuku = %{version}
 
%description poshuku-pintab
Poshuku PinTab allows to pin selected Poshuku tabs so that they cannot be closed until unpinned.

%package poshuku-onlinebookmarks
Summary:        LeechCraft Online Bookmarks Module
Requires:       %{name}-poshuku = %{version}
 
%description poshuku-onlinebookmarks
Online bookmarks plugin for LeechCraft.
 
This package contains a plugin for the Poshuku web browser that allows
to synchronize bookmarks with services like Read It Later.

%package poshuku-pintab
Summary:        LeechCraft Pintab Module
Requires:       %{name}-poshuku = %{version}
  
%description poshuku-pintab
Poshuku PinTab allows to pin selected Poshuku tabs so that they cannot be
closed until unpinned.

%package poshuku-keywords
Summary:        Support of url keywords for LeechCraft Poshuku browser
Requires:       %{name}-poshuku = %{version}

%description poshuku-keywords
This package contains a plugin for supporting url keywords for LeechCraft
Poshuku browser

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
Requires:       %{name}-secman = %{version}

%description secman-simplestorage
Simple storage backend for SecMan.
 
This package contains a simple, unencrypted storage backend for
SecMan, LeechCraft's security manager plugin.
 
%package azoth
Summary:        LeechCraft Messenger Module
Requires:       %{name} = %{version}
 
%description azoth
IM client for LeechCraft.
 
This package contains a simple IM client for LeechCraft.
 
%package azoth-acetamine
Summary:        IRC support for LeechCraft Azoth Module
Requires:       %{name}-azoth = %{version}
 
%description azoth-acetamine
This package contains a IRC support for LeechCraft Azoth Module.
 
%package azoth-chathistory
Summary:        Chat history for LeechCraft Azoth Module
Requires:       %{name}-azoth = %{version}
 
%description azoth-chathistory
This package contains a chat history module for LeechCraft Azoth
Module.
 
%package azoth-autopaste
Summary:        Autopaste for LeechCraft Azoth Module
Requires:       %{name}-azoth = %{version}
 
%description azoth-autopaste
This package contains an autopaste for automatic pasting of long
messages to pastebins
 
%package azoth-embedmedia
Summary:        Media objects for LeechCraft Azoth Module
Requires:       %{name}-azoth = %{version}
 
%description azoth-embedmedia
This package enables embedding different media objects in chat
tab for LeechCraft Azoth Module.
 
%package azoth-hili
Summary:        Conference highlights for LeechCraft Azoth Module
Requires:       %{name}-azoth = %{version}
 
%description azoth-hili
This package contains a plugin for customizing conference highlights
for LeechCraft Azoth Module.
 
%package azoth-juick
Summary:        Juick.com service for LeechCraft Azoth Module
Requires:       %{name}-azoth = %{version}
 
%description azoth-juick
This package contains a plugin for the juick.com microblogging service
for LeechCraft Azoth Module.
 
%package azoth-nativeemoticons
Summary:        Emoticons packs for LeechCraft Azoth Module
Requires:       %{name}-azoth = %{version}
 
%description azoth-nativeemoticons
This package contains a plugin for supporting emoticons packs in LeechCraft
Azoth Module.
 
%package azoth-p100q
Summary:        Psto.net service for LeechCraft Azoth Module
Requires:       %{name}-azoth = %{version}
 
%description azoth-p100q
This package contains a plugin for the psto.net microblogging service
for LeechCraft Azoth Module.
 
%package azoth-standardstyles
Summary:        Standard styles for LeechCraft Azoth Module
Requires:       %{name}-azoth = %{version}
 
%description azoth-standardstyles
This package provides standard styles for LeechCraft Azoth Module.
 
%package azoth-xoox
Summary:        XMPP support for LeechCraft Azoth Module
Requires:       %{name}-azoth = %{version}
 
%description azoth-xoox
This package contains a XMPP support for LeechCraft Azoth Module.
 
%package azoth-xtazy
Summary:        Publishing current user tune for LeechCraft Azoth Module
Requires:       %{name}-azoth = %{version}
 
%description azoth-xtazy
This package contains a plugin for publishing current user tune for
LeechCraft Azoth Module.
 
%package azoth-depester
Summary:        LeechCraft Azoth Module for ignoring unwanted participants
Requires:       %{name}-azoth = %{version}
 
%description azoth-depester
This package contains LeechCraft Azoth Module for ignoring unwanted participants.
 
%package azoth-herbicide
Summary:        Antispam plugin for LeechCraft Azoth Module
Requires:       %{name}-azoth = %{version}
 
%description azoth-herbicide
This package contains a basic antispam plugin for LeechCraft Azoth Module.
 
%package azoth-rosenthal
Summary:        Spell checker plugin for LeechCraft Azoth Module
Requires:       %{name}-azoth = %{version}
 
%description azoth-rosenthal
This package contains  a spell checker plugin for LeechCraft Azoth Module
 
%package azoth-lastseen
Summary:        Client-side recording of contacts' last online
Requires:       %{name}-azoth = %{version}
 
%description azoth-lastseen
Azoth LastSeen for client-side recording of contacts' last online and
availability time. It doesn't depend on the concrete protocol implementation.
 
%package azoth-adiumstyles
Summary:        Adium styles for Leechcraft Azoth
Requires:       %{name}-azoth = %{version}
 
%description azoth-adiumstyles
Azoth AdiumStyles for, well, support for Adium styles. It is still
experimental and quite basic, but, nevertheless, already usable.
 
%package azoth-autoidler
Summary:        Automatic change of status due to inactivity period
Requires:       %{name}-azoth = %{version}
 
%description azoth-autoidler
Azoth Autoidler for automatic change of status due to inactivity period.
 
%package azoth-metacontacts
Summary:        Metacontacts for Leechcraft Azoth
Requires:       %{name}-azoth = %{version}
 
%description azoth-metacontacts
Metacontacts for Leechcraft Azoth.
 
%package azoth-modnok
Summary:        LaTeX support for LeechCraft Azoth
Requires:       %{name}-azoth = %{version}
 
%description azoth-modnok
Azoth Modnok for inline in-chat LaTeX rendering and display. It doesn't
depend on the underlying protocol, and if the protocol supports rich text
formatting in outgoing messages, it is able to replace the formulas with
corresponding images in outgoing messages as well, so your buddies would
see nice rendered formulas instead of raw LaTeX code, even if their client
doesn't have a LaTeX formatter.
 
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

%if 0%{?fedora} >= 15
%package bittorrent
Summary:    BitTorrent, the BitTorrent client
Requires:   %{name} = %{version}
Requires:   rb_libtorrent-devel >= 0.15.6

%description bittorrent
BitTorrent, the BitTorrent client for LeechCraft.
%endif

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
Advanced Notifications module for more customizable notifications for
Leechcraft.

%package glance
Summary:        Glance feature moved from the Core to a separate plugin
Requires:       %{name} = %{version}
 
%description glance
%{summary}.
 
%package tabslist
Summary:        TabsList for LeechCraft Internet Client
Requires:       %{name} = %{version}
 
%description tabslist
TabsList for showing the list of currently opened tabs and quickly selecting
one of them.

%prep
%setup -q -n %{name}-%{version}

mkdir build 

%build
cd build

%{cmake} \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DLEECHCRAFT_VERSION="%{version}" \
%if 0%{?fedora} < 15
  -DENABLE_TORRENT=False \
%endif
  -DRESPECTLIB64=True \
  -DENABLE_SECMAN=True \
  -DENABLE_POPISHU=True \
  -DENABLE_AZOTH=True \
  -DENABLE_EISKALTDCPP=True \
  -DENABLE_GLANCE=True \
  -DENABLE_TABSLIST=True \
  -DENABLE_ADVANCEDNOTIFICATIONS=True \
  ../src  

make %{?_smp_mflags}

%install
cd build
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f ${RPM_BUILD_ROOT}{_datadir}/icons/oxygen/32x32/actions/.directory
desktop-file-install                                    \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
  %{SOURCE1}

%post
/sbin/ldconfig
 
%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README COPYING INSTALL
%{_bindir}/%{name}
%{_bindir}/%{name}-add-file
%{_datadir}/%{name}/settings/coresettings.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%dir %{_datadir}/icons/hicolor/14x14
%dir %{_datadir}/icons/hicolor/14x14/apps
%{_datadir}/icons/Pevzi
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/icons
%{_datadir}/%{name}/icons/Pevzi.mapping
%dir %{_datadir}/%{name}/installed
%dir %{_datadir}/%{name}/settings
%dir %{_datadir}/%{name}/translations
%dir %{_datadir}/%{name}/scripts
%dir %{_datadir}/%{name}/qml
%{_datadir}/%{name}/translations/leechcraft_??.qm
%{_datadir}/%{name}/translations/leechcraft_??_??.qm
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/*lcutil.so.*
%{_libdir}/*xmlsettingsdialog.so.*
%doc %{_mandir}/man1/%{name}.1.gz

%files advancednotifications
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_advancednotifications.so
%{_datadir}/%{name}/qml/visualnotificationsview.qml
%{_datadir}/%{name}/translations/leechcraft_advancednotifications*

%if 0%{?fedora} >= 15
%files  bittorrent
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_bittorrent.so
%{_datadir}/%{name}/settings/torrentsettings.xml
%{_datadir}/%{name}/translations/%{name}_bittorrent_*.qm
%endif
 
%files  eiskaltdcpp
%defattr(-,root,root,-)
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
 
%files aggregator
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/aggregatorsettings.xml
%{_datadir}/%{name}/translations/%{name}_aggregator*.qm
%{_libdir}/%{name}/plugins/*%{name}_aggregator.so
%{_datadir}/%{name}/scripts/aggregator/
 
%files aggregator-bodyfetch
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_aggregator_bodyfetch.so
 
%files auscrie
%defattr(-,root,root,-)
%{_datadir}/%{name}/translations/%{name}_auscrie_*.qm
%{_libdir}/%{name}/plugins/lib%{name}_auscrie.so
 
%files azoth
%defattr(-,root,root,-)
%{_datadir}/%{name}/azoth
%{_datadir}/%{name}/settings/azothsettings.xml
%{_datadir}/%{name}/translations/%{name}_azoth_en.qm
%{_datadir}/%{name}/translations/%{name}_azoth_??_??.qm
%{_libdir}/%{name}/plugins/*%{name}_azoth.so
 
%files azoth-acetamine
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/azothacetamidesettings.xml
%{_datadir}/%{name}/translations/%{name}_azoth_acetamide*
%{_libdir}/%{name}/plugins/*%{name}_azoth_acetamide.so
 
%files azoth-autopaste
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/azothautopastesettings.xml
%{_datadir}/%{name}/translations/%{name}_azoth_autopaste*
%{_libdir}/%{name}/plugins/*%{name}_azoth_autopaste.so
 
%files azoth-chathistory
%defattr(-,root,root,-)
%{_datadir}/%{name}/translations/%{name}_azoth_chathistory*
%{_libdir}/%{name}/plugins/*%{name}_azoth_chathistory.so
 
%files azoth-embedmedia
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_azoth_embedmedia.so
 
%files azoth-hili
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/azothhilisettings.xml
%{_datadir}/%{name}/translations/%{name}_azoth_hili*
%{_libdir}/%{name}/plugins/*%{name}_azoth_hili.so
 
%files azoth-juick
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_azoth_juick.so
 
%files azoth-nativeemoticons
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_azoth_nativeemoticons.so
 
%files azoth-p100q
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/azothp100qsettings.xml
%{_libdir}/%{name}/plugins/*%{name}_azoth_p100q.so
 
%files azoth-standardstyles
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_azoth_standardstyles.so
 
%files azoth-xoox
%defattr(-,root,root,-)
%{_datadir}/%{name}/translations/%{name}_azoth_xoox*
%{_libdir}/%{name}/plugins/*%{name}_azoth_xoox.so
 
%files azoth-xtazy
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/azothxtazysettings.xml
%{_libdir}/%{name}/plugins/*%{name}_azoth_xtazy.so
%{_datadir}/%{name}/translations/%{name}_azoth_xtazy*
 
%files azoth-depester
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_azoth_depester.so
%{_datadir}/%{name}/translations/%{name}_azoth_depester*
 
%files azoth-herbicide
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_azoth_herbicide.so
%{_datadir}/%{name}/translations/%{name}_azoth_herbicide*
%{_datadir}/%{name}/settings/azothherbicidesettings.xml
 
%files azoth-rosenthal
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_azoth_rosenthal.so
%{_datadir}/%{name}/translations/%{name}_azoth_rosenthal*
%{_datadir}/%{name}/settings/azothrosenthalsettings.xml
 
%files azoth-adiumstyles
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_azoth_adiumstyles*
 
%files azoth-autoidler
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_azoth_autoidler*
%{_datadir}/%{name}/settings/azothautoidlersettings.xml
%{_datadir}/%{name}/translations/leechcraft_azoth_autoidler*
 
%files azoth-lastseen
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_azoth_lastseen*
%{_datadir}/%{name}/translations/leechcraft_azoth_lastseen*
 
%files azoth-metacontacts
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_azoth_metacontacts*
%{_datadir}/%{name}/translations/%{name}_azoth_metacontacts*
 
%files azoth-modnok
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_azoth_modnok*
%{_datadir}/%{name}/settings/azothmodnoksettings.xml
%{_datadir}/%{name}/translations/leechcraft_azoth_modnok*
%{_bindir}/lc_azoth_modnok_latexconvert.sh
 
%files cstp
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/cstpsettings.xml
%{_datadir}/%{name}/translations/leechcraft_cstp*.qm
%{_libdir}/%{name}/plugins/*leechcraft_cstp.so
 
%files dbusmanager
%defattr(-,root,root,-)
%{_datadir}/%{name}/translations/leechcraft_dbusmanager*.qm
%{_libdir}/%{name}/plugins/*leechcraft_dbusmanager.so
%{_datadir}/%{name}/settings/dbusmanagersettings.xml
 
%files deadlyrics
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/deadlyricssettings.xml
%{_datadir}/%{name}/translations/%{name}_deadlyrics*.qm
%{_libdir}/%{name}/plugins/*%{name}_deadlyrics.so
 
%files devel
%defattr(-,root,root,-)
%{_datadir}/%{name}/cmake
%{_includedir}/%{name}
%{_libdir}/*lcutil.so
%{_libdir}/*xmlsettingsdialog.so
 
%files historyholder
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*leechcraft_historyholder.so
%{_datadir}/%{name}/translations/leechcraft_historyholder*.qm
 
%files iconset-oxygen
%defattr(-,root,root,-)
%{_datadir}/icons/oxygen/*/*/*
%{_datadir}/%{name}/icons/oxygen.mapping
 
%files iconset-tango
%defattr(-,root,root,-)
%{_datadir}/%{name}/icons/Tango.mapping
 
%files kinotify
%defattr(-,root,root,-)
%{_datadir}/%{name}/kinotify
%{_datadir}/%{name}/settings/kinotifysettings.xml
%{_libdir}/%{name}/plugins/*%{name}_kinotify.so
 
%files lmp
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/lmpsettings.xml
%{_datadir}/%{name}/translations/%{name}_lmp*
%{_libdir}/%{name}/plugins/*%{name}_lmp.so
 
%files networkmonitor
%defattr(-,root,root,-)
%{_datadir}/%{name}/translations/%{name}_networkmonitor*.qm
%{_libdir}/%{name}/plugins/*%{name}_networkmonitor.so
 
%files newlife
%defattr(-,root,root,-)
%{_datadir}/%{name}/translations/%{name}_newlife*.qm
%{_libdir}/%{name}/plugins/*%{name}_newlife.so
 
%files poshuku-cleanweb
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/poshukucleanwebsettings.xml
%{_datadir}/%{name}/translations/%{name}_poshuku_cleanweb*.qm
%{_libdir}/%{name}/plugins/*%{name}_poshuku_cleanweb.so
 
%files poshuku-filescheme
%defattr(-,root,root,-)
%{_datadir}/%{name}/translations/%{name}_poshuku_filescheme_*.qm
%{_libdir}/%{name}/plugins/*%{name}_poshuku_filescheme.so
 
%files poshuku-pintab
%defattr(-,root,root,-)
%_libdir/%{name}/plugins/*_poshuku_pintab.so
 
%files poshuku-keywords
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_poshuku_keywords.so
%{_datadir}/%{name}/settings/poshukukeywordssettings.xml
 
%files poshuku-fua
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/poshukufuasettings.xml
%{_datadir}/%{name}/translations/%{name}_poshuku_fua*.qm
%{_libdir}/%{name}/plugins/*%{name}_poshuku_fua.so
 
%files popishu
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/popishusettings.xml
%{_datadir}/%{name}/translations/%{name}_popishu_*.qm
%{_libdir}/%{name}/plugins/*%{name}_popishu.so
 
%files poshuku
%defattr(-,root,root,-)
%{_datadir}/%{name}/installed/poshuku/
%{_datadir}/%{name}/settings/poshukusettings.xml
%{_datadir}/%{name}/translations/%{name}_poshuku_??.qm
%{_datadir}/%{name}/translations/%{name}_poshuku_??_??.qm
%{_libdir}/%{name}/plugins/*%{name}_poshuku.so
 
%files poshuku-fatape
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/poshukufatapesettings.xml
%{_libdir}/%{name}/plugins/*%{name}_poshuku_fatape.so
%{_datadir}/%{name}/translations/leechcraft_poshuku_fatape_*.qm
 
%files poshuku-wyfv
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/poshukuwyfvsettings.xml
%{_datadir}/%{name}/translations/%{name}_poshuku_wyfv*.qm
%{_libdir}/%{name}/plugins/*%{name}_poshuku_wyfv.so
 
%files poshuku-onlinebookmarks
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/poshukuonlinebookmarkssettings.xml
%{_datadir}/%{name}/translations/%{name}_poshuku_onlinebookmarks*.qm
%{_libdir}/%{name}/plugins/*%{name}_poshuku_onlinebookmarks.so
 
%files secman
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_secman.so
 
%files secman-simplestorage
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_secman_simplestorage.so
 
%files seekthru
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/seekthrusettings.xml
%{_datadir}/%{name}/translations/%{name}_seekthru*.qm
%{_libdir}/%{name}/plugins/*%{name}_seekthru.so
 
%files shellopen
%defattr(-,root,root,-)
%{_datadir}/%{name}/translations/%{name}_shellopen*.qm
%{_libdir}/%{name}/plugins/*%{name}_shellopen.so
 
%files summary
%defattr(-,root,root,-)
%{_datadir}/%{name}/translations/%{name}_summary*.qm
%{_libdir}/%{name}/plugins/*%{name}_summary.so
 
%files tabpp
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/tabppsettings.xml
%{_datadir}/%{name}/translations/%{name}_tabpp_*.qm
%{_libdir}/%{name}/plugins/*%{name}_tabpp.so
 
%files vgrabber
%defattr(-,root,root,-)
%{_datadir}/%{name}/settings/vgrabbersettings.xml
%{_datadir}/%{name}/translations/%{name}_vgrabber*.qm
%{_libdir}/%{name}/plugins/*%{name}_vgrabber.so
 
%files glance
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_glance.so
%{_datadir}/%{name}/translations/leechcraft_glance*
 
%files tabslist
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/*%{name}_tabslist.so
%{_datadir}/%{name}/translations/leechcraft_tabslist*

%changelog
* Mon Jul 25 2011 Minh Ngo <nlminhtl@gmail.com> 0.4.85
- new packages: tabslist, glance, poshuku-pintab, azoth-modnok,
- azoth-metacontacts, azoth-lastseen, azoth-adiumstyles,
- azoth-autoidler
* Mon Jul 04 2011 Minh Ngo <nlminhtl@gmail.com> - 0.4.80-0.1
- 0.4.80 release
- azoth depester plugin
- azoth herbicide plugin
- azoth rosenthal plugin
* Mon Jun 06 2011 Minh Ngo <nlminhtl@gmail.com> - 0.4.75-0.1.gitga29292b
- initial build 
