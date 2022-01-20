#!/bin/bash

# ECLIPSEDIR=/opt/eclipse-clp

java -Declipse.directory=$ECLIPSEDIR -jar lib/UMLtoCSP.jar $*
