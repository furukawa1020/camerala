%% his.cls by Hirotake Ishii, based on his.sty by Tetsuya Yoshida, based on jvrst.sty by Ichigaya Atsuro, based on ieicej.sty
\typeout{his.cls; Version 1.1 [Sep. 19, 2017]}

\newif\ifNTTfont
\@ifundefined{kanjiskip}{\NTTfonttrue
 \let\kanjiskip=\jintercharskip
 \let\xkanjiskip=\jasciikanjiskip
 \def\bf{\protect\pdg\protect\pbf}
 }{\NTTfontfalse}

\newif\if@AmSTexFont
\@ifundefined{shape}{\@AmSTexFontfalse}{\@AmSTexFonttrue}

\newif\ifphototype
%   \phototypetrue  % for phototypesetting, using SAKEN fonts
%   \phototypefalse % for author, using CM fonts and min10 etc.
\newif\ifProof % for adjustment of the top and bottom of text
%   \Prooftrue \overfullrule 5pt
%   \Prooffalse
\newif\ifJIScodechange % for \MARU{?}
%   \JIScodechangetrue % exchange MaruSuuji produced by \MARU{?} to Shaken
% Code
%   \JIScodechangefalse

\newif\ifBoldMath
        \BoldMathtrue
%       \BoldMathfalse

% Add for Latex2e Oct. 22. 2006
\DeclareOldFontCommand{\mc}{\normalfont\mcfamily}{\mathmc}
\DeclareOldFontCommand{\gt}{\normalfont\gtfamily}{\mathgt}
\DeclareOldFontCommand{\rm}{\normalfont\rmfamily}{\mathrm}
\DeclareOldFontCommand{\sf}{\normalfont\sffamily}{\mathsf}
\DeclareOldFontCommand{\tt}{\normalfont\ttfamily}{\mathtt}
\DeclareOldFontCommand{\bf}{\normalfont\bfseries}{\mathbf}
\DeclareOldFontCommand{\it}{\normalfont\itshape}{\mathit}
\DeclareOldFontCommand{\sl}{\normalfont\slshape}{\@nomath\sl}
\DeclareOldFontCommand{\sc}{\normalfont\scshape}{\@nomath\sc}
\DeclareRobustCommand*{\cal}{\@fontswitch\relax\mathcal}
\DeclareRobustCommand*{\mit}{\@fontswitch\relax\mathnormal}

\def\@ptsize{0}
\@namedef{ds@11pt}{\def\@ptsize{1}}
\@namedef{ds@12pt}{\def\@ptsize{2}}
\def\ds@twoside{\@twosidetrue \@mparswitchtrue}
\def\ds@draft{\overfullrule 5pt}
\@options

\@twosidetrue
\@mparswitchtrue

\lineskip 2pt \normallineskip 2pt
\def\baselinestretch{1}

\newdimen\h@
  \h@=0.25mm
\newdimen\JQ % for SK fonts
  \JQ=0.7392507pt
\newdimen\Q % for SE fonts
  \Q=0.71144pt
\newdimen\@bs
  \@bs=19\h@

% for micro TeX
\ifNTTfont\else
 \@ifundefined{inhibitglue}{\let\<=\relax }{}
\fi

\ifBoldMath
\def\@mbiix{cmmib9}
\def\@mbiviii{cmmib8}
\def\@mbivii{cmmib7}
\def\@mbivi{cmmib6}
\def\@mbiv{cmmib5}
\def\@mbsyix{cmbsy9}
\def\@mbsyviii{cmbsy8}
\def\@mbsyvii{cmbsy7}
\def\@mbsyvi{cmbsy6}

\@ifundefined{@ptscale}{\def\@ptscale#1{ scaled #100}}{}

 \font\fivmib = cmmib10 at 5pt % bold math italic
 \font\fivsyb = cmbsy10 at 5pt % bold math symbols
 \font\fivlyb = lasyb10 \@ptscale5 % LaTeX symbols

\let\original@vipt=\vipt
\def\vipt{\original@vipt
  \def\unboldmath{\everymath{}\everydisplay{}\@nomath\unboldmath
          \textfont\@ne\sixmi 
          \textfont\tw@\sixsy \textfont\lyfam\sixly
          \@boldfalse}\@boldfalse
  \def\boldmath{\@ifundefined{sixmib}{\global\font\sixmib\@mbivi 
   \global\font\sixsyb\@mbsyvi
   \global\font\sixlyb\@lasyb\@ptscale6\relax\@addfontinfo\@vipt
   {\def\boldmath{\everymath{\mit}\everydisplay{\mit}\@prtct\@nomathbold
        \textfont\@ne\sixmib 
        \textfont\tw@\sixsyb 
        \textfont\lyfam\sixlyb \@prtct\@boldtrue}}}{}\@vipt\boldmath}%
  \def\ptt{\@getfont\ptt\ttfam\@vipt{cmtt10
 \@ptscale6}\@nohyphens\ptt\@vipt}%
}

\let\original@viipt=\viipt
\def\viipt{\original@viipt
  \def\unboldmath{\everymath{}\everydisplay{}\@nomath\unboldmath
          \textfont\@ne\sevmi 
          \textfont\tw@\sevsy \textfont\lyfam\sevly
          \@boldfalse}\@boldfalse
  \def\boldmath{\@ifundefined{sevmib}{\global\font\sevmib\@mbivii 
   \global\font\sevsyb\@mbsyvii
   \global\font\sevlyb\@lasyb\@ptscale7\relax\@addfontinfo\@viipt
   {\def\boldmath{\everymath{\mit}\everydisplay{\mit}\@prtct\@nomathbold
        \textfont\@ne\sevmib %% \scriptfont\@ne\sixmib
 \scriptscriptfont\@ne\fivmib 
        \textfont\tw@\sevsyb %% \scriptfont\tw@\sixsyb
 \scriptscriptfont\tw@\fivsyb 
        \textfont\lyfam\sevlyb \@prtct\@boldtrue}}}{}\@viipt\boldmath}%
  \def\ptt{\@getfont\ptt\ttfam\@viipt{cmtt10
 \@ptscale7}\@nohyphens\ptt\@viipt}%
}

\let\original@viiipt=\viiipt
\def\viiipt{\original@viiipt
  \def\unboldmath{\everymath{}\everydisplay{}\@nomath\unboldmath
          \textfont\@ne\egtmi 
          \textfont\tw@\egtsy \textfont\lyfam\egtly
          \@boldfalse}\@boldfalse
  \def\boldmath{\@ifundefined{egtmib}{\global\font\egtmib\@mbiviii 
   \global\font\egtsyb\@mbsyviii 
   \global\font\egtlyb\@lasyb\@ptscale8\relax\@addfontinfo\@viiipt
   {\def\boldmath{\everymath{\mit}\everydisplay{\mit}\@prtct\@nomathbold
        \textfont\@ne\egtmib %% \scriptfont\@ne\sixmib
 \scriptscriptfont\@ne\fivmib 
        \textfont\tw@\egtsyb %% \scriptfont\tw@\sixsyb
 \scriptscriptfont\tw@\fivsyb 
        \textfont\lyfam\egtlyb \@prtct\@boldtrue}}}{}\@viiipt\boldmath}%
  \def\ptt{\@getfont\ptt\ttfam\@viiipt{cmtt8}\@nohyphens\ptt\@viiipt}%
}

\let\original@ixpt=\ixpt
\def\ixpt{\original@ixpt
  \def\unboldmath{\everymath{}\everydisplay{}\@nomath\unboldmath
          \textfont\@ne\ninmi 
          \textfont\tw@\ninsy \textfont\lyfam\ninly
          \@boldfalse}\@boldfalse
  \def\boldmath{\@ifundefined{ninmib}{\global\font\ninmib\@mbiix
   \global\font\ninsyb\@mbsyix 
   \global\font\ninlyb\@lasyb\@ptscale9\relax\@addfontinfo\@ixpt
   {\def\boldmath{\everymath{\mit}\everydisplay{\mit}\@prtct\@nomathbold
        \textfont\@ne\ninmib %% \scriptfont\@ne\sevmib
 \scriptscriptfont\@ne\fivmib 
        \textfont\tw@\ninsyb %% \scriptfont\tw@\sevsyb
 \scriptscriptfont\tw@\fivsyb 
        \textfont\lyfam\ninlyb \@prtct\@boldtrue}}}{}\@ixpt\boldmath}%
}
\fi

\ifNTTfont
 \jfont\fivmin = dm5
 \jfont\sixmin = dm6
 \jfont\sevmin = dm7
 \jfont\egtmin = dm8
 \jfont\ninmin = dm9
 \jfont\tenmin = dm10
 \jfont\elvmin = dm10  scaled 1095 % about 15\JQ
 \jfont\twlmin = dm10  scaled 1200 % about 18\JQ

 \jfont\fivgt = dg5
 \jfont\sixgt = dg6
 \jfont\sevgt = dg7
 \jfont\egtgt = dg8
 \jfont\ningt = dg9
 \jfont\tengt = dg10
 \jfont\elvgt = dg10 scaled 1095
 \jfont\twlgt = dg10 scaled 1200

 \let\cntrm\relax
 \let\cntit\relax
 \let\cntbf\relax

 \let\EFhead\relax
 \font\EFnomble=cmss8
 \font\EFfoot=cmss8
 \jfont\KFsec=dg10 % about 14\JQ
 \font\EFsec=cmbx10
 \jfont\KFtype=dm10 scaled 1728 % about 24\JQ
\else
 \let\dg\gt
 \let\dm\mc
 \let\pdg\pgt
 \let\pdm\pmc
 \ifphototype
  \input ieicejfn.sty % "load Shaken fonts"
 \else
  \let\cntrm\relax
  \let\cntit\relax
  \let\cntbf\relax
  \let\EFhead\relax

  \font\EFnomble=cmss8
  \font\EFfoot=cmss8
  \font\KFsec=goth10 at 14\JQ
  \font\EFsec=cmbx10
  \font\KFtype=min10 at 24\JQ

  \font\fivmin = min10 at 7\JQ
  \font\sixmin = min10 at 9\JQ
  \font\sevmin = min10 at 10\JQ
  \font\egtmin = min10 at 11\JQ
  \font\ninmin = min10 at 12\JQ
  \font\tenmin = min10 at 13\JQ
  \font\elvmin = min10 at 15\JQ
  \font\twlmin = min10 at 18\JQ

  \font\fivgt = goth10 at 7\JQ
  \font\sixgt = goth10 at 9\JQ
  \font\sevgt = goth10 at 10\JQ
  \font\egtgt = goth10 at 11\JQ
  \font\ningt = goth10 at 12\JQ
  \font\tengt = goth10 at 13\JQ
 \fi
\fi

%% Changed : \@normalsize -> \normalsize for Latex2e Oct. 22. 2006
%% \def\normalsize{\@setsize\normalsize{14.7pt plus1pt minus1pt}{9.5pt}{9.5pt} %% For 24x49, but will get warning.
\def\normalsize{\@setsize\normalsize{15pt plus1pt minus1pt}\xpt\@xpt
\abovedisplayskip 10pt plus2pt minus5pt\belowdisplayskip \abovedisplayskip
\abovedisplayshortskip \z@ plus3pt\belowdisplayshortskip 6pt plus3pt
minus3pt\let\@listi\@listI} 

\def\small{\@setsize\small{11pt}\ixpt\@ixpt
\abovedisplayskip 8.5pt plus 3pt minus 4pt\belowdisplayskip
 \abovedisplayskip
\abovedisplayshortskip \z@ plus2pt\belowdisplayshortskip 4pt plus2pt minus
 2pt
\def\@listi{\leftmargin\leftmargini \topsep 4pt plus 2pt minus 2pt\parsep
 2pt
plus 1pt minus 1pt
\itemsep \parsep}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
%\def\footnotesize{\@setsize\footnotesize{9pt}\ixpt\@ixpt}
%
\def\footnotesize{\@setsize\footnotesize{8pt}\viiipt\@viiipt}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\abovedisplayskip 6pt plus 2pt minus 4pt\belowdisplayskip \abovedisplayskip
\abovedisplayshortskip \z@ plus 1pt\belowdisplayshortskip 3pt plus 1pt minus
2pt

\def\@listi{\leftmargin\leftmargini \topsep 3pt plus 1pt minus 1pt\parsep
 2pt
plus 1pt minus 1pt
\itemsep \parsep}

\def\Small{\@setsize\Small{16\h@}\viiipt\@viiipt}
\def\scriptsize{\@setsize\scriptsize{8pt}\viipt\@viipt}
\def\tiny{\@setsize\tiny{6pt}\vpt\@vpt}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
%\def\large{\@setsize\large{18pt}\xpt\@xpt}
%\def\Large{\@setsize\Large{18pt}\xivpt\@xivpt}
%\def\LARGE{\@setsize\LARGE{18pt}\xviipt\@xviipt}
%
\def\large{\@setsize\large{12pt}\xpt\@xpt}
\def\Large{\@setsize\Large{14pt}\xivpt\@xivpt}
\def\LARGE{\@setsize\LARGE{16pt}\xviipt\@xviipt}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\huge{\@setsize\huge{25pt}\xxpt\@xxpt}
\def\Huge{\@setsize\Huge{30pt}\xxvpt\@xxvpt}
\normalsize 

%% set of style parameters
\oddsidemargin-5.4mm%\z@
\evensidemargin-5.4mm%\z@
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
%\topmargin-5.4mm%\z@
\topmargin-3.4mm%\z@

\textwidth=170mm%24x2+30\h@
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
%\textheight=25.3cm%43\@bs
\textheight=25.2cm%43\@bs

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
%\advance \textheight by \topskip  \textheight=25.3cm
\advance \textheight by \topskip  \textheight=25.2cm
%
%\headheight=11\h@
\headsep=4.75mm
\footskip=7.5mm
%% \footheight=12\h@ % Comment out for Latex2e Oct. 22. 2006
\unitlength=1mm
\baselineskip=19\h@
\parindent=1zw
\columnsep=10mm
\fboxrule=.1mm
\fboxsep=.5zw
\parskip\z@

\marginparwidth 20mm
\marginparsep 5mm

\skip\footins 1\@bs plus 4pt minus 2pt 
\intextsep 12pt plus 2pt minus 2pt
% \@maxsep 20pt			% Comment out for Latex2e Oct. 22. 2006
% \@dblmaxsep 20pt 		% Comment out for Latex2e Oct. 22. 2006
\@fptop 0pt plus 1fil \@fpsep 8pt plus 2fil \@fpbot 0pt plus 1fil 
\@dblfptop 0pt plus 1fil \@dblfpsep 8pt plus 2fil \@dblfpbot 0pt plus 1fil
\marginparpush 5pt

\def\topfraction{1}
\def\bottomfraction{1}
\def\textfraction{0}
\def\floatpagefraction{0}
\def\dbltopfraction{1}
\def\dblfloatpagefraction{0}
\setcounter{topnumber}{5}
\setcounter{dbltopnumber}{3}
\setcounter{bottomnumber}{3}
\setcounter{totalnumber}{5}
\floatsep 1\@bs plus 1.5mm minus 2mm
\dblfloatsep 1\@bs plus 1.5mm minus 2mm
\textfloatsep 1.5\@bs plus 2mm minus 3mm
\dbltextfloatsep 1.5\@bs plus 2mm minus 3mm

\partopsep 2pt plus 1pt minus 1pt 
\@lowpenalty 51 \@medpenalty 151 \@highpenalty 301 
\@beginparpenalty -\@lowpenalty \@endparpenalty -\@lowpenalty \@itempenalty
-\@lowpenalty 


%% redefinition of "\@startsection" is based on ipsjpaper.sty
\def\@startsection#1#2#3#4#5#6{\if@noskipsec \leavevmode \fi
   \par \@tempskipa #4\relax
   \@afterindenttrue
   \ifdim \@tempskipa <\z@ \@tempskipa -\@tempskipa \@afterindentfalse\fi
   \if@nobreak \everypar{}\else
    \addpenalty{\@secpenalty}%
     \ifnum #2=\@ne
       \vskip-\prevdepth \prevdepth\z@ \vskip\baselineskip
       \advance\@tempskipa-\baselineskip \vspace*{\@tempskipa}%
     \else\addvspace{\@tempskipa}\fi\fi \@ifstar
     {\@ssect{#3}{#4}{#5}{#6}}{\@dblarg{\@sect{#1}{#2}{#3}{#4}{#5}{#6}}}}

\newbox\Secbox
\newif\ifjidori\jidoritrue
% \@sect{NAME}{LEVEL}{INDENT}{BEFORESKIP}{AFTERSKIP}{STYLE}[ARG1]{ARG2}
\def\@sect#1#2#3#4#5#6[#7]#8{%
\ifnum #2>\c@secnumdepth%
 \def\@svsec{}%
\else
 \refstepcounter{#1}
 \ifnum #2=3\relax% 
  \if@AmSTexFont
   \edef\@svsec{\cntbf\csname the#1\endcsname\hskip 1em }\else
   \edef\@svsec{\cntbf \csname the#1\endcsname\hskip 1em }\fi
 \else
  \edef\@svsec{\csname the#1\endcsname\hskip 1em }
 \fi
\fi%
 \@tempskipa #5\relax%
  \ifdim \@tempskipa>\z@%
   \begingroup #6\relax%
    \setbox\Secbox\hbox{#8}%
     \ifjidori%
      \ifdim \wd\Secbox < 5zw%
       \@hangfrom{\hskip #3\relax\@svsec}%
        {\interlinepenalty \@M \kintou{5zw}{#8}\par}%
      \else%
       \@hangfrom{\hskip #3\relax\@svsec}{\interlinepenalty \@M #8\par}%
      \fi%
     \else% \jidorifalse
      \@hangfrom{\hskip #3\relax\@svsec}{\interlinepenalty \@M #8\par}%
     \fi%
   \endgroup
  \else
   \def\@svsechd{#6\hskip #3\@svsec #8
     \csname #1mark\endcsname{#7}
     \addcontentsline{toc}{#1}{\ifnum #2>\c@secnumdepth \else
       \protect\numberline{\csname the#1\endcsname}\fi
        #7}%
    }
  \fi
\@xsect{#5}}

\def\@ssect#1#2#3#4#5{\@tempskipa #3\relax
\ifdim \@tempskipa>\z@
 \begingroup #4
  \setbox\Secbox\hbox{#5}%
   \ifjidori
    \ifdim \wd\Secbox < 5zw
     \@hangfrom{\hskip #1}{\interlinepenalty \@M \kintou{5zw}{#5}\par}
    \else
     \@hangfrom{\hskip #1}{\interlinepenalty \@M #5\par}
    \fi
   \else%jidorifalse
    \@hangfrom{\hskip #1}{\interlinepenalty \@M #5\par}
   \fi
 \endgroup
\else
 \def\@svsechd{#4\hskip #1\relax #5}
\fi
\@xsect{#3}}

\def\section{\@startsection{section}{1}{\z@}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
%
% {0.001\baselineskip plus .1mm minus .1mm}
% {.5\baselineskip plus .1mm minus .1mm}{\normalsize\bf\cntbf}}
%
 {0.5\baselineskip plus .5mm minus .5mm}
 {0.5\baselineskip plus .5mm minus .5mm}{\centering\large\bf\cntbf }}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\subsection{\@startsection{subsection}{2}{1zw}
 {0.001\baselineskip plus .1mm minus .1mm}
 {0.001\baselineskip plus .1mm minus .1mm}{\normalsize\bf\cntbf}}
\def\subsubsection{\@startsection{subsubsection}{3}{1zw}
  {0.001\baselineskip plus .1mm minus .1mm}{0.001\baselineskip plus .1mm
 minus .1mm}
  {\normalsize\rm\cntrm}}
\def\paragraph{\@startsection
 {paragraph}{4}{\z@}{0.001\baselineskip plus .1mm}
 {0.001\baselineskip plus .1mm}{\normalsize\rm\cntrm}}
\def\subparagraph{\@startsection
 {subparagraph}{4}{\parindent}{0.001\baselineskip plus .1mm}
 {0.001\baselineskip plus .1mm}{\normalsize\rm\cntrm}}

\setcounter{secnumdepth}{3}

\def\appendix{\par
 \def\section{\@startsection {section}{1}{\z@}
  {0.5\baselineskip plus.5mm minus.5mm}
  {0.5\baselineskip plus.5mm minus.5mm}{\centering\Large\KFsec\EFsec}}
 \section*{Appendix}
  \def\section{\@startsection{section}{1}{1zw}
   {0.0001\baselineskip plus.1mm minus.1mm}
   {0.0001\baselineskip plus.1mm minus.1mm}{\normalsize\bf\cntbf}}
 \setcounter{section}{0}
 \setcounter{subsection}{0}
 \setcounter{equation}{0}
 \setcounter{figure}{0}
 \setcounter{table}{0}
 \def\theequation{\mbox{\rm A$\cdot$\arabic{equation}}}
 \def\thefigure{A$\cdot$\,\@arabic\c@figure}
 \def\thetable{A$\cdot$\,\@arabic\c@table}
}

\leftmargini 2zw
\leftmarginii 2zw 
\leftmarginiii 2zw 
\leftmarginiv 2zw 
\leftmarginv 2zw
\leftmarginvi 2zw
\leftmargin\leftmargini
\labelsep 1zw
\labelwidth\leftmargini\advance\labelwidth-\labelsep
\def\@listI{\leftmargin\leftmargini \parsep 4pt plus 2pt minus 1pt\topsep
 8pt
plus 2pt minus 4pt\itemsep 4pt plus 2pt minus 1pt}
%%\def\@listI{\leftmargin\leftmargini \parsep 0pt plus 1pt minus 1pt\topsep
% 0pt
%%plus 1pt minus 1pt\itemsep 0pt plus 1pt minus 1pt}
\let\@listi\@listI
\@listi 
\def\@listii{\leftmargin\leftmarginii
 \labelwidth\leftmarginii\advance\labelwidth-\labelsep
 \topsep 0pt plus 1pt minus 1pt
 \parsep 0pt plus 1pt minus 1pt
 \itemsep \parsep}
\def\@listiii{\leftmargin\leftmarginiii
 \labelwidth\leftmarginiii\advance\labelwidth-\labelsep
 \topsep 0pt plus 1pt minus 1pt 
 \parsep \z@ \partopsep 0pt plus 0pt minus 1pt
 \itemsep \topsep}
\def\@listiv{\leftmargin\leftmarginiv
 \labelwidth\leftmarginiv\advance\labelwidth-\labelsep}
\def\@listv{\leftmargin\leftmarginv
 \labelwidth\leftmarginv\advance\labelwidth-\labelsep}
\def\@listvi{\leftmargin\leftmarginvi
 \labelwidth\leftmarginvi\advance\labelwidth-\labelsep}

\def\labelenumi{\theenumi.}
\def\theenumi{\arabic{enumi}} 
\def\labelenumii{\theenumii.}
\def\theenumii{\alph{enumii}}
\def\p@enumii{\theenumi}
\def\labelenumiii{\theenumiii.}
\def\theenumiii{\roman{enumiii}}
\def\p@enumiii{\theenumi(\theenumii)}
\def\labelenumiv{\theenumiv.}
\def\theenumiv{\Alph{enumiv}} 
\def\p@enumiv{\p@enumiii\theenumiii}

\def\labelitemi{$\bullet$}
\def\labelitemii{\bf --}
\def\labelitemiii{$\ast$}
\def\labelitemiv{$\cdot$}


\newskip\@qqvsep
\@qqvsep=.5\baselineskip plus 1mm minus .5mm

\def\verse{\let\\=\@centercr 
 \list{}{%
  \topsep\@qqvsep \parsep\z@\partopsep\z@
  \itemsep\z@
  \itemindent -1zw
  \listparindent \itemindent 
  \rightmargin\leftmargin\advance\leftmargin 1zw}
  \item[]}
\let\endverse\endlist

\def\quotation{\list{}{%
 \topsep\@qqvsep \parsep\z@\partopsep\z@
 \listparindent 1zw
 \itemindent\listparindent
 \rightmargin\leftmargin}%
 \item[]}
\let\endquotation=\endlist

\def\quote{\list{}{%
 \topsep\@qqvsep \parsep\z@\partopsep\z@
 \rightmargin\leftmargin}%
 \item[]}
\let\endquote=\endlist

\def\theequation{\arabic{equation}}

\arraycolsep 5pt
\tabcolsep 0.5zw
\arrayrulewidth .1mm
\doublerulesep \z@
\tabbingsep \labelsep 

\skip\@mpfootins = \skip\footins

%\newcommand{\atlist}[3]{
%       #1\raisebox{0.2ex}{\scriptsize\footnotemark[1]#2}
%       \footnotetext[#2]{#3}
%}

% \newcounter{part}
\newcounter {section}
\newcounter {subsection}[section]
\newcounter {subsubsection}[subsection]
\newcounter {paragraph}[subsubsection]
\newcounter {subparagraph}[paragraph]

% \def\thepart{\Roman{part}}
\def\thesection{\arabic{section}.}
\def\thesubsection{\arabic{section}.\,\arabic{subsection}}
\def\thesubsubsection{\thesubsection.\,\arabic{subsubsection}}
\def\theparagraph{\thesubsubsection.\,\arabic{paragraph}}
\def\thesubparagraph{\theparagraph.\,\arabic{subparagraph}}


\def\thebibliography#1{%
 \def\subsection{\@startsection{subsection}{2}{\z@}
  {1.5\baselineskip plus 1mm minus 0.5mm}{0.15\@bs plus 1mm}{\centering\bf}}
\subsection*{Reference}
\small\ninmin\cntrm\baselineskip=15\h@
 \list{[\arabic{enumi}]}{\settowidth\labelwidth{亜亜}%
  \leftmargin=3zw% \leftmargin\labelwidth \advance\leftmargin\labelsep
  \labelsep=1zw
  \usecounter{enumi}}
 \itemsep=\z@\parskip=\z@
 \def\newblock{\hskip .11em plus .33em minus .07em}
 \sloppy\clubpenalty-100\widowpenalty-100%%
 \clubpenalty4000\widowpenalty4000
 \sfcode`\.=1000\relax}

\def\endthebibliography{\endlist
\par
\vskip-\topsep
\vskip-\partopsep
\vskip-\parskip
}

\newif\if@restonecol

\def\footnoterule{\kern-3\p@
 \hrule height .1mm width \columnwidth
 \kern 2.715\p@}

% \@addtoreset{footnote}{page}

\long\def\@makefntext#1{%\footnotesize\sixmin\cntrm
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
%
% \advance\leftskip by 3zw %	左を3文字分空ける
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \parindent 1zw
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \noindent\hbox{\kern-.5zw \@thefnmark{}\kern-.5zw\makebox[1zw][c]{：}}#1}
% \noindent\hbox{\kern-.5zw \@thefnmark{}\kern-.5zw\makebox[2zw][c]{：}}#1}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%\def\@makefnmark{\hbox{$^{\mbox{\tiny \kern-.5zw
% \@thefnmark{}\kern-.5zw}}$}}
%
\def\@makefnmark{\hbox{$^{\mbox{\hspace{1mm}\scriptsize \@thefnmark{}}}$}}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\def\thefootnote{\arabic{footnote}}

% Center env. without additional vertical glue
\def\Center{\itemsep\z@\topsep\z@\parsep\z@\partopsep\z@\trivlist\Centering\item[]}
\def\Centering{\let\\=\@centercr\rightskip\@flushglue\leftskip\@flushglue
\parindent\z@\parfillskip\z@}
\let\endCenter=\endtrivlist

\def\HANG#1#2{\hangindent=#1\hangafter=#2\relax}

\newbox\@capnumbox
\newbox\@tempboxb
\newdimen\capwidth
\newdimen\@abovecaptionskip
\newdimen\@belowcaptionskip

\long\def\@caption#1[#2]#3{\par
\begingroup
 \@parboxrestore
 \small
 \@makecaption{\csname fnum@#1\endcsname}{\ignorespaces #3}\par
\endgroup}

\long\def\@makecaption#1#2{\vskip\@abovecaptionskip
\small\ninmin\cntrm
\setbox\@capnumbox\hbox{#1\hskip1zw\mbox{}}
\setbox\@tempboxa\hbox{#1\hskip1zw #2}
 \ifdim \wd\@tempboxa > \capwidth% hsize
  \hfil\begin{minipage}[t]{\capwidth}%
  \HANG{\wd\@capnumbox}{1}#1\hskip1zw #2%
  \end{minipage}\vskip2\h@
 \else
  \setbox\@tempboxb\hbox{#2}
   \ifdim \wd\@tempboxb < 5zw
    \hbox to\hsize{\hfil#1\hskip1zw\kintou{5zw}{#2}\hfil}
   \else
    \hbox to\hsize{\hfil\box\@tempboxa\hfil}
   \fi
 \fi
}

\newdimen\ecapwidth
\long\def\ecaption#1{\small\cntrm
\setbox\@capnumbox\hbox{\csname fnum@e\@captype\endcsname\hskip1zw\mbox{}}
\setbox\@tempboxa\hbox{\csname fnum@e\@captype\endcsname\hskip1zw #1}
 \ifdim \wd\@tempboxa > \ecapwidth% \hsize
  \hfil\begin{minipage}[t]{\ecapwidth}
   \HANG{\wd\@capnumbox}{1}%
   \csname fnum@e\@captype\endcsname\hskip1zw #1
  \end{minipage}\par
 \else
  \hbox to\hsize{\hfil\box\@tempboxa\hfil}
 \fi
\vspace{\@belowcaptionskip}}


%% based on macro defined by styuse.sty
\newsavebox{\@parc@ption}
\def\parcaption#1{\small\sevmin\cntrm%
    \sbox{\@parc@ption}{\shortstack[l]{#1}}%
    \setbox\@tempboxa\hbox{\csname fnum@\@captype\endcsname\hskip1zw}%
%   \@tempdima\columnwidth \advance\@tempdima-\wd\@tempboxa
    \@tempdima\capwidth \advance\@tempdima-\wd\@tempboxa%
    \@tempdimb .97\@tempdima%<-- maximum length is set here
    \ifdim\wd\@parc@ption>\@tempdimb \@tempdima\@tempdimb%
     \else\@tempdima\wd\@parc@ption\fi%
    \sbox{\@tempboxa}{\parbox[t]{\@tempdima}{#1}}%
    \caption{\usebox{\@tempboxa}}\vskip2\h@}

\def\parecaption#1{\small\cntrm%
    \sbox{\@parc@ption}{\shortstack[l]{#1}}%
    \setbox\@tempboxa\hbox{\csname fnum@e\@captype\endcsname\hskip1zw}%
%   \@tempdima\columnwidth \advance\@tempdima-\wd\@tempboxa
    \@tempdima\ecapwidth \advance\@tempdima-\wd\@tempboxa
    \@tempdimb .97\@tempdima
    \ifdim\wd\@parc@ption>\@tempdimb \@tempdima\@tempdimb
     \else\@tempdima\wd\@parc@ption\fi
    \sbox{\@tempboxa}{\parbox[t]{\@tempdima}{#1}}%
    \ecaption{\usebox{\@tempboxa}}}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%\def\fnum@figure{図\thefigure }
%% \def\fnum@table{{\bf\sevgt\cntbf 表\thetable}}
%\def\fnum@table{表\thetable}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\def\fnum@figure{Fig.\,\thefigure}
\def\fnum@table{Table \thetable}


%\def\fnum@efigure{Fig.\,\thefigure}
%\def\fnum@etable{Table \thetable}

\def\tableenv{\def\@setstrut{\setbox\strutbox=%
 \hbox{\vrule \@height .72\baselineskip \@depth .28\baselineskip
 \@width\z@}}
 \small\sevmin\cntrm
 \let\center=\Center}%% \ifphototype\let\tt=\sevtt\else\fi

\newcounter{figure}
\def\thefigure{\@arabic\c@figure}
\def\fps@figure{tbp}
\def\ftype@figure{1}
\def\ext@figure{lof}
\def\figure{\bgroup\tableenv\capwidth=65mm\ecapwidth=65mm
 \@abovecaptionskip=10pt\@belowcaptionskip\z@\@float{figure}}
\def\endfigure{\end@float\egroup}
%\let\endfigure\end@float
\@namedef{figure*}{\bgroup\tableenv\capwidth=.66\textwidth\ecapwidth=.66\textwidth
 \@abovecaptionskip=10pt\@belowcaptionskip\z@\@dblfloat{figure}}
\@namedef{endfigure*}{\end@dblfloat\egroup}

\newcounter{table}
\def\thetable{\@arabic\c@table}
\def\fps@table{tbp}
\def\ftype@table{2}
\def\ext@table{lot}
\def\table{\bgroup\tableenv\capwidth=65mm\ecapwidth=65mm
 \@abovecaptionskip\z@\@belowcaptionskip=3pt\@float{table}}
\def\endtable{\end@float\egroup}
%\let\endtable\end@float
\@namedef{table*}{\bgroup\tableenv\capwidth=.66\textwidth\ecapwidth=.66\textwidth
 \@abovecaptionskip\z@\@belowcaptionskip=3pt\@dblfloat{table}}
\@namedef{endtable*}{\end@dblfloat\egroup}

\def\@fnsymbol#1{\ifcase#1\or\dagger \or\dagger\dagger \or
\dagger\dagger\dagger \or
\dagger\dagger\dagger\dagger \or
\dagger\dagger\dagger\dagger\dagger \or
\dagger\dagger\dagger\dagger\dagger\dagger \or
* \or** \or*** \else\@ctrerr\fi\relax}


%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
%\def\jtitle{\@ifnextchar[{\d@jtitle}{\s@jtitle}}
%\def\d@jtitle[#1]#2{\gdef\@TITLE{#1}\gdef\@jtitle{#2}}
%\def\s@jtitle#1{\gdef\@TITLE{#1}\gdef\@jtitle{#1}}
%\def\@jtitle{}
%\def\@TITLE{}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
%\def\etitle#1{\gdef\@etitle{#1}}
%\def\@etitle{}
%
\def\etitle{\@ifnextchar[{\d@etitle}{\s@etitle}}
\def\d@etitle[#1]#2{\gdef\@TITLE{#1}\gdef\@etitle{#2}}
\def\s@etitle#1{\gdef\@TITLE{#1}\gdef\@etitle{#1}}
\def\@etitle{}
\def\@TITLE{}

\def\jtitle#1{\gdef\@jtitle{#1}}
\def\@jtitle{}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
\def\jauthor#1{\gdef\@jauthor{#1}}
\def\@jauthor{}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
%\def\@AUTHOR{}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\def\eauthor#1{\gdef\@eauthor{#1}}
\def\@eauthor{}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
\def\@AUTHOR{}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
%\def\etitle#1{\gdef\@etitle{#1}}
%\def\@etitle{}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newbox\abstractbox
\newbox\keywordbox
\setbox\abstractbox\hbox{}
\setbox\keywordbox\hbox{}
\def\abstract{\global\setbox\abstractbox=\hbox\bgroup%
\begin{minipage}[t]{145mm}
{\small\baselineskip=8\h@\bf
{\normalsize\bf Abstract }\, --\hskip1zw}\small\bf\ignorespaces}
\def\endabstract{\end{minipage}\egroup}
\def\keyword{\global\setbox\keywordbox=\hbox\bgroup%
\begin{minipage}[t]{145mm}
{\small\baselineskip=16\h@\bf 
{\normalsize\bf Keywords }\, :\hskip1zw}\small\bf\ignorespaces}
\def\endkeyword{\end{minipage}\egroup}

\def\maketitle{\par
 \begingroup
 \def\thefootnote{*\arabic{footnote}}
 \def\@makefnmark{\hbox 
 to 7pt{$^{\@thefnmark}$\hss}} 
 \twocolumn[\@maketitle]
%
 \thispagestyle{vr}\@thanks 
% \thispagestyle{his}\@thanks 
%
 \endgroup
 \setcounter{footnote}{0}
 \let\maketitle\relax
 \let\@maketitle\relax
 \gdef\@thanks{}\gdef\@jauthor{}\gdef\@jtitle{}%
\gdef\@eauthor{}\gdef\@etitle{}
\let\thanks\relax}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%	Title
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\def\@maketitle{\newpage
 \null
 \vskip 2em \begin{center}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% {\LARGE\bf \@jtitle \par} \vskip 1.0em 
% {\etitlesize\bf \@etitle \par} \vskip 1.0em 
 {\Large\bf \@etitle \par} \vskip 1.0em 
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
%{\Large \lineskip .5em
{\large \lineskip .5em
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%\begin{tabular}[t]{c}\@jauthor 
\begin{tabular}[t]{c}\@eauthor
% 
 \end{tabular}\par}  \vskip 1.0em 
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% {\large\bf \@etitle \par} \vskip .5em
%\setcounter{footnote}{0}
%{\large \lineskip .5em
%\begin{tabular}[t]{c}\@eauthor
% \end{tabular}\par}\par
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\vskip 2em {\normalsize
\usebox{\abstractbox}\hfill
 \vskip17\h@
\usebox{\keywordbox}
 }\vskip 17\h@
%\vspace{\@ADJ}
\end{center}
% \par
\vskip 1.0em} 

\newcount\year@cnt
\def\YEAR#1{\def\@tempa{#1}
 \ifx \@tempa\empty \year@cnt=1995\gdef\@YEAR{1995}\else
  \year@cnt=#1\gdef\@YEAR{#1}\fi
 \ifnum \year@cnt <1990\relax \gdef\@YEAR{19#1} \else 
  \advance\year@cnt by-1990\relax \fi
 \gdef\h@YEAR{\the\year@cnt}
}

\def\page#1{\def\@tempa{#1}
 \ifx \@tempa\empty
        \setcounter{page}{1}    
 \else
        \setcounter{page}{#1}
 \fi
}

\newcounter{subpage}
\def\thesubpage{\arabic{subpage}}
\def\PAGE#1{\def\@tempa{#1}
 \ifx \@tempa\empty
        \setcounter{subpage}{\value{page}}      
 \else
        \setcounter{subpage}{#1}
 \fi
}

\def\MONTH#1{\def\@tempa{#1}
 \ifx \@tempa\empty \gdef\@MONTH{xx}
 \else 
  \gdef\@MONTH{#1}
\fi}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%\def\TYPE#1{\gdef\@TYPE{#1}
% \def\@tempa{#1}\def\@tempb{\bf 原著論文}
%  \ifx \@tempa\@tempb\gdef\h@TYPE{\bf 原著論文}\else
%   \gdef\h@TYPE{\bf 論\hskip1zw 文}\fi}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\TYPE#1{\def\@tempa{#1}
 \ifx \@tempa\empty \gdef\@TYPE{xx}
 \else 
  \gdef\@TYPE{#1}
\fi}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\def\VOL#1{\def\@tempa{#1}
 \ifx \@tempa\empty \gdef\@VOL{xx}
 \else 
  \gdef\@VOL{#1}
\fi}

\def\NO#1{\def\@tempa{#1}
 \ifx \@tempa\empty \gdef\@NO{xx}
\else 
 \gdef\@NO{#1}
\fi}

\def\AUTHOR#1{\def\@tempa{#1}
 \ifx \@tempa\empty \gdef\@AUTHOR{xx}
 \else
        \gdef\@AUTHOR{#1}
 \fi}

\def\Sissue#1{\gdef\@Sissue{#1}}
\def\@Sissue{}
\def\@VOL{}
\def\@TYPE{}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%	h@TYPEを使わないこと
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%\def\h@TYPE{}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\def\@YEAR{}
\def\h@YEAR{}
\def\@MONTH{}
\def\@NO{}
\def\@AUTHOR{}
\MONTH{xx}
\YEAR{96}

\mark{{}{}}
\def\@RH{\rlap{\smash{\raisebox{-1\headsep}{\rule{0.01mm}{10mm}\rule{10mm}{0.01mm}}}}}
\def\@LH{\llap{\smash{\raisebox{-1\headsep}{\rule{10mm}{0.01mm}\rule{0.01mm}{10mm}}}}}
\def\@RB{\rlap{\smash{\raisebox{1\footskip}{\rule[-10mm]{0.01mm}{10mm}\rule{10mm}{0.01mm}}}}}
\def\@LB{\llap{\smash{\raisebox{1\footskip}{\rule{10mm}{0.01mm}\rule[-10mm]{0.01mm}{10mm}}}}}


\def\ps@vr{\let\@mkboth\@gobbletwo
 \def\hrulefill{\leaders\hrule height-1.5mm depth1.75mm\hfill}
\def\@oddhead{\ifProof\@LH\else\fi%
%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%	h@TYPEを使わないこと
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%\rlap{\raisebox{-3mm}{\underline{\Large\h@TYPE}}}\hfill \llap{\normalsize 
% Vol.%\@VOL\, No.\@NO ,\,\@YEAR }
\rlap{\raisebox{-3mm}{\underline{\large\@TYPE}}}\hfill \llap{\normalsize 
 Vol.\@VOL\, No.\@NO ,\,\@YEAR }
%
 \ifProof\@RH\else\fi }

\def\@evenhead{\ifProof\@RH\else\fi%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%	h@TYPEを使わないこと
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% \rlap{\normalsize Vol.\@VOL\, No.\@NO ,\,\@YEAR
% }\hfill\llap{\raisebox{-3mm}{\%underline{\Large\h@TYPE}}}
 \rlap{\normalsize Vol.\@VOL\, No.\@NO ,\,\@YEAR
 }\hfill\llap{\raisebox{-3mm}{\underline{\Large\@TYPE}}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 \ifProof\@RH\else\fi}
%\def\@oddfoot{\ifProof\@LB\else\fi%
%  \hfill {\Small\thepage}\hfill
% \ifProof\@RB\else\fi}%
%\def\@evenfoot{\ifProof\@LB\else\fi%
% \hfill{\Small\thepage}\hfill
% \ifProof\@RB\else\fi}
}


%\def\ps@VR{\let\@mkboth\@gobbletwo%
\def\ps@HIS{\let\@mkboth\@gobbletwo%
%
\def\@oddhead{\ifProof\@LH\else\fi%
%\addtocounter{subpage}{1}%
%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
% \hfill{\Small\bf \@AUTHOR\, :\,\@TITLE }\hfill
%
 \hfill{\Small\bf \,\@TITLE }\hfill
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% \llap{\Small \thesubpage}
 \ifProof\@RH\else\fi
}%
\def\@evenhead{\ifProof\@LH\else\fi%
%\addtocounter{subpage}{1}%
% \rlap{\Small \thesubpage}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
 \hfill{\Small\bf The Transactions of Human Interface Society\hskip1zw
% \hfill{\Small\bf Transactions of Human Interface Society\hskip1zw
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 Vol.\@VOL ,\, No.\@NO ,\,\@YEAR}\hfill
 \ifProof\@RH\else\fi}
}
\def\@oddfoot{\ifProof\@LB\else\fi%
% \hfill{\Small \thepage}\hfill
 \ifProof\@RB\else\fi}
\def\@evenfoot{\ifProof\@LB\else\fi%
% \hfill{\Small \thepage}\hfill
 \ifProof\@RB\else\fi}

\def\today{\ifcase\month\or
 January\or February\or March\or April\or May\or June\or
 July\or August\or September\or October\or November\or December\fi
 \space\number\day, \number\year}


%\ps@plain \pagenumbering{arabic} \onecolumn
 \if@twoside\else\raggedbottom\fi 
%% redefintion of eqnarray; from fleqn.sty
\def\[{\relax\ifmmode\@badmath\else
\parsep 4pt plus 2pt minus 1pt \topsep 8pt plus 2pt minus 4pt \itemsep 4pt
 plus 2pt minus 1pt
\begin{trivlist}\item[]\leavevmode
 \hbox to\linewidth\bgroup$ \displaystyle
 \hskip\mathindent\bgroup\fi}
\def\]{\relax\ifmmode \egroup $\hfil \egroup \end{trivlist}\else \@badmath
 \fi}

\def\equation{\refstepcounter{equation}
\parsep 4pt plus 2pt minus 1pt \topsep 8pt plus 2pt minus 4pt \itemsep 4pt
 plus 2pt minus 1pt
\trivlist \item[]\leavevmode
 \hbox to\linewidth\bgroup $ \displaystyle
\hskip\mathindent}
\def\endequation{$\hfil \displaywidth\linewidth\@eqnnum\egroup \endtrivlist}

\def\eqnarray{\stepcounter{equation}
\parsep 4pt plus 2pt minus 1pt \topsep 8pt plus 2pt minus 4pt \itemsep 4pt
 plus 2pt minus 1pt
\let\@currentlabel=\theequation
\global\@eqnswtrue
\global\@eqcnt\z@\tabskip\mathindent\let\\=\@eqncr
\abovedisplayskip\topsep\ifvmode\advance\abovedisplayskip\partopsep\fi
\belowdisplayskip\abovedisplayskip
\belowdisplayshortskip\abovedisplayskip
\abovedisplayshortskip\abovedisplayskip
$$\halign to
\linewidth\bgroup\@eqnsel\hskip\@centering$\displaystyle\tabskip\z@
 {##}$&\global\@eqcnt\@ne \hskip .8\arraycolsep \hfil${##}$\hfil%% default 2\arraycolsep
 &\global\@eqcnt\tw@ \hskip .8\arraycolsep $\displaystyle{##}$\hfil 
 \tabskip\@centering&\llap{##}\tabskip\z@\cr}
\def\endeqnarray{\@@eqncr\egroup
 \global\advance\c@equation\m@ne$$\global\@ignoretrue }
\newdimen\mathindent 
\mathindent = 3mm

\def\@eqnnum{(\theequation)\hspace*{3mm}}

%% from "citesort.sty", with a little modified
\newcount\@minsofar
\newcount\@min
\newcount\@cite@temp
\def\@citex[#1]#2{%
\if@filesw \immediate \write \@auxout {\string \citation {#2}}\fi
\@tempcntb\m@ne \let\@h@ld\relax \def\@citea{}%
\@min\m@ne%
\@cite{%
  \@for \@citeb:=#2\do {\@ifundefined {b@\@citeb}%
    {\@h@ld\@citea\@tempcntb\m@ne{\bf ?}%
    \@warning {Citation `\@citeb ' on page \thepage \space undefined}}%
{\@minsofar\z@ \@for \@scan@cites:=#2\do {%
  \@ifundefined{b@\@scan@cites}%
    {\@cite@temp\m@ne}
    {\@cite@temp\number\csname b@\@scan@cites \endcsname \relax}%
\ifnum\@cite@temp > \@min% select the next one to list
    \ifnum\@minsofar = \z@
      \@minsofar\number\@cite@temp
      \edef\@scan@copy{\@scan@cites}\else
    \ifnum\@cite@temp < \@minsofar
      \@minsofar\number\@cite@temp
      \edef\@scan@copy{\@scan@cites}\fi\fi\fi}\@tempcnta\@min
  \ifnum\@minsofar > \z@ % some more
    \advance\@tempcnta\@ne
    \@min\@minsofar
    \ifnum\@tempcnta=\@minsofar %   Number follows previous--hold on to it
      \ifx\@h@ld\relax
        \edef \@h@ld{\@citea\csname b@\@scan@copy\endcsname}%
      \else \edef\@h@ld{\ifmmode{]～[}\else]～[\fi\csname
 b@\@scan@copy\endcsname}%
      \fi
    \else \@h@ld\@citea\csname b@\@scan@copy\endcsname
          \let\@h@ld\relax
  \fi % no more
\fi}%
\def\@citea{],\penalty\@highpenalty\,[}}\@h@ld}{#1}}
%% end of citesort.sty

\def\@cite#1#2{\leavevmode\unskip
  \ifnum\lastpenalty=\z@\penalty\@highpenalty\fi% highpenalty before
  \,$^{\mbox{\scriptsize [{\multiply\@highpenalty 3 #1
			% triple-highpenalties within
      \if@tempswa,\penalty\@highpenalty\ #2\fi % and before note.
    }]}}$\spacefactor\@m}



\newcommand{\namelistlabel}[1]{\mbox{#1}\hfil}
\newenvironment{namelist}[1]{
\begin{list}{} 
 {\let\makelabel\namelistlabel 
 \settowidth{\labelwidth}{#1} 
 \setlength{\leftmargin}{1.1\labelwidth}}}
{\end{list}}


\def\LaTeX{{\rm L\kern-.36em\raise.3ex\hbox{$\scriptstyle {\rm
 A}$}\kern-.15em
    T\kern-.1667em\lower.7ex\hbox{E}\kern-.125emX}}
\@ifundefined{AmSTeX}
   {\def\AmSTeX{\leavevmode\hbox{$\cal A\kern-.2em\lower.376ex%
        \hbox{$\cal M$}\kern-.2em\cal S$-\TeX}}}{}
\@ifundefined{AmSLaTeX}
   {\def\AmSLaTeX{\leavevmode\hbox{$\cal A\kern-.2em\lower.376ex%
        \hbox{$\cal M$}\kern-.2em\cal S$-\LaTeX}}}{}
\@ifundefined{BibTeX}
   {\def\BibTeX{{\rm B\kern-.05em{\sc i\kern-.025em b}\kern-.08em%
    T\kern-.1667em\lower.7ex\hbox{E}\kern-.125emX}}}{}
\@ifundefined{SliTeX}
   {\def\SliTeX{{\rm S\kern-.06emL\kern-.18em\raise.32ex\hbox
                {\sc i}\kern -.03em\TeX}}}{}
\@ifundefined{JTeX}
  {\def\JTeX{\leavevmode\lower.5ex\hbox{J}\kern-.17em\TeX}}{}
\@ifundefined{JLaTeX}
  {\def\JLaTeX{\leavevmode\lower.5ex\hbox{\rm J}\kern-.17em\LaTeX}}{}
\@ifundefined{JBibTeX}
  {\def\JBibTeX{\leavevmode\lower.6ex\hbox{\rm J}\kern-.15em\BibTeX}}{}

%% some definitions
\def\FRAC#1#2{\leavevmode\kern-.1em
  \raise.5ex\hbox{\the\scriptfont0 #1}\kern-.1em
  /\kern-.15em\lower.25ex\hbox{\the\scriptfont0 #2}}
\def\RN#1{\uppercase\expandafter{\romannumeral#1}}
\def\onelineskip{\par\vspace{1\baselineskip}\par}
\def\halflineskip{\par\vspace{.5\baselineskip}\par}
\def\Onelineskip{\par\vspace*{1\baselineskip}\par}
\def\Halflineskip{\par\vspace*{.5\baselineskip}\par}
\def\kintou#1#2{\@ifundefined{jintercharskip}%
 {\makebox[#1]{\kanjiskip\z@ plus 1fill minus 1fill\xkanjiskip=\kanjiskip
 #2}}%
 {\makebox[#1]{\jintercharskip=0pt plus 1fill minus 1fill 
 \jasciikanjiskip=\jintercharskip #2}}}
\def\doubledash{\hbox to 2zw{---\hss ---}}
\def\ruby#1#2{\leavevmode\vbox{\baselineskip\z@skip\lineskip.25ex
 \ialign{##\crcr\tiny\hfill#1\hfill\crcr\hfill#2\hfill\crcr}}}

\def\leq{\mathrel{\mathpalette\gl@align<}} \let\le=\leq
\def\geq{\mathrel{\mathpalette\gl@align>}} \let\ge=\geq
\def\gl@align#1#2{\lower.6ex\vbox{\baselineskip\z@skip\lineskip\z@
 \ialign{$\m@th#1\hfil##\hfil$\crcr#2\crcr=\crcr}}}
\def\subseteq{\rlap{\raisebox{.25ex}{$\subset$}}\raisebox{-1.1ex}{$=$}}
\def\supseteq{\rlap{\raisebox{.25ex}{$\supset$}}\raisebox{-1.1ex}{$=$}}
\def\neq{\mathrel{\mathpalette\c@ncelass=}}
\def\c@ncelass#1#2{\ooalign{$\hfil#1\mkern-.4mu|\hfil$\crcr$#1#2$}}
\let\ne=\neq

\def\QED{{\unskip\nobreak\hfil\penalty50
 \hskip1zw\hbox{}\nobreak\hfil \hbox{$\Box$\hskip1zw}
 \parfillskip\z@ \finalhyphendemerits\z@\par}}

\def\Hline{\noalign{\hrule height 0.4mm}}

\ifNTTfont\else
 \prebreakpenalty`"=10000
 \prebreakpenalty`）=10000
 \postbreakpenalty`（=10000
\fi

\hbadness4000
\vbadness10001
\tolerance 9999 \pretolerance\m@ne


\pagenumbering{arabic}
\twocolumn
\sloppy
%
%\pagestyle{VR}
\pagestyle{HIS}
%

\def\itemize{\ifnum \@itemdepth >3 \@toodeep\else \advance\@itemdepth \@ne
\edef\@itemitem{labelitem\romannumeral\the\@itemdepth}%
\list{\csname\@itemitem\endcsname}{\def\makelabel##1{\hss\llap{##1}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%		
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%\leftmargin1zw\labelwidth1zw\labelsep=1zw\itemindent2zw
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\listparindent=1zw
\itemsep\z@\topsep\z@\parsep\z@\partopsep\z@}\fi}
\let\enditemize =\endlist


\def\enumerate{\ifnum \@enumdepth >3 \@toodeep\else
      \advance\@enumdepth \@ne 
      \edef\@enumctr{enum\romannumeral\the\@enumdepth}\list
      {\csname label\@enumctr\endcsname}{\usecounter
        {\@enumctr}\def\makelabel##1{\hss\llap{##1}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
%\leftmargin1zw\labelwidth2zw\labelsep1zw\itemindent2zw
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\listparindent=1zw
\itemsep\z@\topsep\z@\parsep\z@\partopsep\z@
\clubpenalty-200}\fi}
\let\endenumerate =\endlist

\def\descriptionlabel#1{\hspace\labelsep #1}
\def\description{\list{}{
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	modified from jvrst.sty
%
%\leftmargin1zw\labelsep1zw\labelwidth\z@ %\itemindent-\leftmargin
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\listparindent=1zw
\itemsep\z@\topsep\z@\parsep\z@\partopsep\z@
\let\makelabel\descriptionlabel}}
\let\enddescription\endlist

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%	for profile
%		modified from ieice.sty
%

\def\HANG#1#2{\hangindent=#1 \hangafter=#2\relax}
\newcounter{PROFILE}
\newdimen\@heightofprofile
\newbox\@profile


\long\def\profile#1#2{%
 \refstepcounter{PROFILE}%
 \ifnum\thePROFILE >1%
  \relax%
 \else%
  \vspace{21mm}\par
 \fi%
 \parindent\z@%
  \setbox\@profile\hbox{%
  \begin{minipage}[t]{\columnwidth}%
   \footnotesize\baselineskip=3.5mm%
    \ifCMR\relax%
    \else%
     \noindent\rlap{\smash{\begin{picture}(25,33)%
     \put(-30,-31){\framebox(25,33){\null}}\end{picture}}}%
    \fi%
    \HANG{30mm}{-11}{\small\bf\tmsbf #1}\hskip 6mm
    {\small\rm\tmsrm #2}\end{minipage}}%
     \@heightofprofile=\ht\@profile%
     \advance \@heightofprofile by \dp\@profile%
      \ifdim \@heightofprofile < 33mm%
       \vbox{\rule[-31mm]{0mm}{33mm}\box\@profile}%
      \else%
       \ifCMR \relax%
       \else%
         \noindent\rlap{\smash{\begin{picture}(25,33)%
         \put(-30,-31){\framebox(25,33){\null}}\end{picture}}}%
       \fi%
        \footnotesize\baselineskip=3.5mm%
        \HANG{30mm}{-11}{\small\bf\tmsbf #1}\hskip 6mm {\small\rm\tmsrm #2}%
      \fi%
\par\vspace{10mm}}

%% paper only
\newenvironment{biography}{\par
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
 \raggedbottom
%
%		受付日と本文の間が、すこし狭いように思えるから
%
% \vskip-3.75mm
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%	@uketsuke IS  defined and used in this style file
%
% \begin{flushright}
 \hfill{\small \@uketsuke}
% \end{flushright}
%
 \begin{center}
 \subsection*{Biography}
 \end{center}
%
}{\par}

\newdimen\@heightofprofile
\newbox\@profile


 \long\def\profile#1#2#3{%

  \small\baselineskip 15\h@
  \vspace{5mm}\par
  \leftskip8\h@
  \parindent=\z@
 \if #1m \def\p@membership{（Member）\kern-.5zw}\else
  \if #1s \def\p@membership{（Student Member）\kern-.5zw}\else
   \if #1h \def\p@membership{（Honorary Member）\kern-.5zw}\else
    \if #1n \def\p@membership{}\else
  \def\p@membership{}
  \typeout{Warning: Check the 1st. argument of \string\profile{#1}{#2}{}.}
 \fi\fi\fi\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

  \def\@checkname{#2}
  \setbox\@tempboxa\hbox{\spaceskip=100mm #2}
  \ifdim \wd\@tempboxa < 100mm
   \typeout{Warning: Profile's name "#2" doesn't have a space.}
   \let\@tempa=\@checkname
  \else
   \setbox\@tempboxa\hbox{#2}
    \ifdim \wd\@tempboxa > 5zw
     \def\@tempb##1 ##2\@nil{##1\hskip1zw ##2}
    \else
     \def\@tempb##1 ##2\@nil{\leavevmode\hbox to 5zw{##1\hfil ##2}}%
    \fi
   \edef\@tempa{\expandafter\@tempb\@checkname\@nil\null}%
  \fi

{\normalsize\leavevmode\hbox{{\bf\cntbf \@tempa}\hskip1zw
     \p@membership}\nobreak}
\\
\begin{minipage}[t]{24mm}%
  \leavevmode\lower32.0mm
  \vbox to 30mm{\hrule height .1mm
    \hbox to 22mm{\vrule width .1mm height 29.8mm%
     \hss
    \vrule width .1mm height 29.8mm}%
  \hrule height .1mm}%
\end{minipage}
\hfill
\begin{minipage}[t]{17zw}
  \hskip1zw\vskip0zw
    #3\par
\end{minipage} 
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%	
%	use uketsuke
%
\def\@uketsuke{\par\hfill （\@received\@revised ）\kern-.5zw\hskip1zw\mbox{}}

\def\received#1#2#3{
	\gdef\@received{received #2 #3, #1}\gdef\@receivedyear{#1}}
\def\revised#1#2#3{\gdef\@revisedyear{#1}%
 \ifx\@receivedyear\@revisedyear
 \gdef\@revised{，revised #2 #3}\else
 \gdef\@revised{，revised #2 #3, #1}\fi
}
\def\@revised{}
\received{x}{xx}{xx}


