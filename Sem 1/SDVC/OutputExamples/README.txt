This directory shows several examples of the translation of UML/OCL models into CSPs. 
The first file is a translation of the class diagram with all OCL constraints:

- FullExample.ecl

The other files provide translation of individual OCL constraints to provide a better
insight of the translation process. Also, to better illustrate these constraints, the
multiplicities of the associations have been modified to make the model satisfiable.

- AuthorsOfStudentPapers.ecl
- NoSelfReviews.ecl
- NoStudentReviewsers.ecl
- PaperLength.ecl

The output files can be solved using the ECLiPSe Constraint Programming System
available at [www.eclipse-clp.org]. To solve one of these files:
- Download and install the latest version of the ECLiPSe constraint solver
- Open the ECLiPSe GUI, based on Tcl-Tk.
- Select "Compile..." and choose an ".ecl file
- Write "findSolutions(Instances)" as the goal. 
- ECLiPSe will respond with "No" if the problem is unfeasible and with "Yes" 
(plus an instantiation of the model) if the problem is feasible.


