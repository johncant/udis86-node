%module UDis86

%{

#include <inttypes.h>
#include <stdlib.h>
#include "/usr/local/include/libudis86/types.h"
#include "/usr/local/include/libudis86/itab.h"
#include "/usr/local/include/libudis86/extern.h"

%}


%include <inttypes.i>
%include "/usr/local/include/libudis86/types.h"
%include "/usr/local/include/libudis86/itab.h"
%include "/usr/local/include/libudis86/extern.h"


%include <node.i>
%node(UDis86)
