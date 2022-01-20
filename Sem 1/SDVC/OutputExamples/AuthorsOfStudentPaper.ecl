% Constraint AuthorsOfStudentPaper
%   This paper shows the translation of a single constraint of the problem 
%   The multiplicities of associations have been modified to make the model
%   satisfiable


:-lib(ic).
:-lib(apply).
:-lib(apply_macros).
:-lib(lists).

:- local struct(researcher(oid,isStudent)).
:- local struct(paper(oid,studentPaper)).

:- local struct(reviews(submission,referee)).
:- local struct(writes(manuscript,author)).

findSolutions(Instances):-

	% Cardinality Definition 
	SResearcher::0..5, SPaper::0..5, 
	SReviews::0..10, SWrites::0..10, 
	CardVariables=[SResearcher, SPaper, SReviews, SWrites],


	constraintsReviewsCard(CardVariables),
	constraintsWritesCard(CardVariables),

	% Cardinality Instantiation
	labeling(CardVariables),

	%Object Creation
	creationResearcher(OResearcher, SResearcher, AtResearcher),
	creationPaper(OPaper, SPaper, AtPaper),

	differentOidsResearcher(OResearcher),
	differentOidsPaper(OPaper),


	%Relationship Creation
	creationReviews(LReviews, SReviews, PReviews, SPaper, SResearcher),
	creationWrites(LWrites, SWrites, PWrites, SPaper, SResearcher),

	differentLinksReviews(LReviews),
	differentLinksWrites(LWrites),

	Instances = [OResearcher, OPaper, LReviews, LWrites],

	cardinalityLinksReviews(Instances),
	cardinalityLinksWrites(Instances),

	% General Constraints
	authorsOfStudentPaper(Instances),

	AllAttributes = [AtResearcher, AtPaper, PReviews, PWrites],
	flatten(AllAttributes, Attributes),

	% Properties Instantiation
	labeling(Attributes).


index("Researcher", 1).
index("Paper", 2).
index("Reviews", 3).
index("Writes", 4).

attIndex("Researcher", "isStudent", 2).
attIndex("Paper", "studentPaper", 2).

roleIndex("Reviews", "submission", 1).
roleIndex("Reviews", "referee", 2).
roleIndex("Writes", "manuscript", 1).
roleIndex("Writes", "author", 2).

roleType("Reviews", "submission", "Paper").
roleType("Reviews", "referee", "Researcher").
roleType("Writes", "manuscript", "Paper").
roleType("Writes", "author", "Researcher").

roleMin("Reviews", "submission", 0).
roleMin("Reviews", "referee", 0).
roleMin("Writes", "manuscript", 0).
roleMin("Writes", "author", 2).

roleMax("Reviews", "submission", 1).
roleMax("Reviews", "referee", 3).
roleMax("Writes", "manuscript", 1).
roleMax("Writes", "author", 2).

assocIsUnique("Reviews", 1).
assocIsUnique("Writes", 1).

constraintsReviewsCard(CardVariables):-constraintsBinAssocMultiplicities("Reviews", "submission", "referee", CardVariables).
constraintsWritesCard(CardVariables):-constraintsBinAssocMultiplicities("Writes", "manuscript", "author", CardVariables).

creationResearcher(Instances, Size, Attributes):-
	length(Instances, Size),
	(foreach(Xi, Instances), fromto([],AtIn,AtOut,Attributes), param(Size) do
		Xi=researcher{oid:Integer1,isStudent:Boolean2}, Integer1::1..Size, Boolean2::0..1, 
		append([Integer1,Boolean2],AtIn, AtOut)).

creationPaper(Instances, Size, Attributes):-
	length(Instances, Size),
	(foreach(Xi, Instances), fromto([],AtIn,AtOut,Attributes), param(Size) do
		Xi=paper{oid:Integer1,studentPaper:Boolean2}, Integer1::1..Size, Boolean2::0..1, 
		append([Integer1,Boolean2],AtIn, AtOut)).

%Sempre que mantenim l'oid com a primer elemet de l'struct
differentOidsResearcher(Instances) :- differentOids(Instances).
differentOidsPaper(Instances) :- differentOids(Instances).


creationReviews(Instances, Size, Participants, SPaper, SResearcher):-
	length(Instances, Size),
	(foreach(Xi, Instances), fromto([],AtIn,AtOut,Participants), param(SPaper), param(SResearcher) do
		Xi=reviews{submission:ValuePart1,referee:ValuePart2}, ValuePart1#>0, ValuePart1#=<SPaper, ValuePart2#>0, ValuePart2#=<SResearcher,
		append([ValuePart1, ValuePart2],AtIn, AtOut)).

creationWrites(Instances, Size, Participants, SPaper, SResearcher):-
	length(Instances, Size),
	(foreach(Xi, Instances), fromto([],AtIn,AtOut,Participants), param(SPaper), param(SResearcher) do
		Xi=writes{manuscript:ValuePart1,author:ValuePart2}, ValuePart1#>0, ValuePart1#=<SPaper, ValuePart2#>0, ValuePart2#=<SResearcher,
		append([ValuePart1, ValuePart2],AtIn, AtOut)).

differentLinksReviews(X):- differentLinks(X).
differentLinksWrites(X):- differentLinks(X).

cardinalityLinksReviews(Instances):-
	linksConstraintMultiplicities(Instances, "Reviews","submission","referee").
cardinalityLinksWrites(Instances):-
	linksConstraintMultiplicities(Instances, "Writes","manuscript","author").

nallInstances1AuthorsOfStudentPaper( Instances,_, Result):-
	ocl_allInstances(Instances, "Paper", Result).

nVariable2_1_1AuthorsOfStudentPaper( _, Vars, Result):-
	ocl_variable(Vars,1,Result).

nAttribute2_1AuthorsOfStudentPaper( Instances, Vars, Result):-
	nVariable2_1_1AuthorsOfStudentPaper(_, Vars, Object),
	ocl_attributeCall(Intances, "Paper", "studentPaper", Object, Result).

nVariable2_2_1_1AuthorsOfStudentPaper( _, Vars, Result):-
	ocl_variable(Vars,1,Result).

nNavigation2_2_1AuthorsOfStudentPaper( Instances, Vars, Result):-
	nVariable2_2_1_1AuthorsOfStudentPaper(Instances, Vars, Value1),
	ocl_navigation(Instances, "Writes", "manuscript", "author", Value1, Result).

nVariable2_2_2_1AuthorsOfStudentPaper( _, Vars, Result):-
	ocl_variable(Vars,1,Result).

nAttribute2_2_2AuthorsOfStudentPaper( Instances, Vars, Result):-
	nVariable2_2_2_1AuthorsOfStudentPaper(_, Vars, Object),
	ocl_attributeCall(Intances, "Researcher", "isStudent", Object, Result).

nexists2_2AuthorsOfStudentPaper( Instances, Vars, Result):-
	nNavigation2_2_1AuthorsOfStudentPaper(Instances, Vars, Value1),
	ocl_col_exists(Instances, Vars, Value1, nAttribute2_2_2AuthorsOfStudentPaper, Result).

nequals2AuthorsOfStudentPaper( Instances, Vars, Result):-
	ocl_boolean_equals(Instances, Vars, nAttribute2_1AuthorsOfStudentPaper, nexists2_2AuthorsOfStudentPaper, Result).

nforAll0AuthorsOfStudentPaper( Instances, Vars, Result):-
	nallInstances1AuthorsOfStudentPaper(Instances, Vars, Value1),
	ocl_col_forAll(Instances, Vars, Value1, nequals2AuthorsOfStudentPaper, Result).

authorsOfStudentPaper(Instances):-
	nforAll0AuthorsOfStudentPaper(Instances, [], Result),
	Result #=1.


% 2007/03/21 
% - orderedObjects: additional code should be added to take care of 
%   floating-point attributes
% - decide where orderedObjects, orderedOids and orderedLinks should be called

%
% ECLiPSe libraries
%
:- lib(ic).     % Interval constraints
:- lib(apply).  % Using variables as functors

%------------------------------------------------------------------------------
%
% Utility methods - methods dealing with oids
% 
%------------------------------------------------------------------------------

% getOid(Object, Oid) :-
%    Get the Oid of an Object. It is always the first field of the struct.

getOid(Object, Oid) :- 
   arg(1, Object, Oid).

% getOidList(ObjectList, OidList) :-
%    OidList is the list of all Oids of Objects, where Objects is
%    a list of objects.

getOidList(ObjectList, OidList) :-
  ( foreach(Object, ObjectList),
    foreach(Oid, OidList)
    do
      getOid(Object, Oid)
  ).

% existsOidInList( ?Oid, ?OidList ):-
%    Constrain an Oid to be a member of an OidList with a known length

existsOidInList(Oid, OidList) :-
   ( foreach(Other, OidList),
     fromto(0, In, Out, Result),
     param(Oid)
     do 
       #=(Oid, Other, Aux),
       ic:or(In, Aux, Out)
   ),
   Result #=1.

% countOidInList( ?OidList, ?Oid, ?Result ) :-
%    Counts the number of times that an Oid appears in OidList 
%    The length of the OidList must be known

countOidInList( OidList, Oid, Result ) :-
   ( foreach(Elem, OidList),
     foreach(TruthValue, Found),
     param(Oid)
     do 
       % TruthValue = 1 if the object has been found, 0 otherwise
       #=(Elem, Oid, TruthValue)
   ),
   Result #= sum(Found).


%------------------------------------------------------------------------------
%
% Constraints on classes - uniqueness of oids, ...
% 
%------------------------------------------------------------------------------

%differentOids(Instances) :-
%   Oids of a class must have a different value 
%   Note: this description is kept for clarity, but it is already
%   implied by the stronger "orderedOids" later

differentOids(Instances):-
   getOidList(Instances, OidList),
   alldifferent(OidList). 

%orderedInstances(Instances) :-
%   All instances of a class must be assigned in increasing order
%   This restriction is imposed for efficiency reasons to avoid
%   exploring all possible permutations within a class

orderedInstances(Instances) :-
  getOidList(Instances, OidList),
  % Oids should fulfill the #< relation
  orderedList(#<, OidList),
  % Attributes should fulfill a less restrictive <= relation
  orderedList(orderForAttributes, Instances).

%orderForAttributes(ObjectA, ObjectB) :-
%   Constrain ObjectA to be less or equal than ObjectB, according to some order.
%   Let at(i,Obj) be the i-th attribute of Obj, then ObjectA is less or equal 
%   than ObjectB if:
%     ( at(1,A) < at(1,B) ) OR
%     ( at(1,A) = at(1,B) AND at(2,A) < at(2,B) ) OR
%     ( at(1,A) = at(1,B) AND at(2,A) = at(2,B) AND at(3,A) < at(3,B) ) OR
%     ...
%     all attributes are equal

orderForAttributes(ObjectA, ObjectB) :-
  ( foreacharg(AttribA, ObjectA), 
    foreacharg(AttribB, ObjectB),
    fromto(0, InOrder, OutOrder, AllLess),
    fromto(1, InEquals, OutEquals, AllEqual),
    count(I,1,_)
    do     
      ( I = 1 -> 

        % Order in Oids is defined differently (see orderedOids)  
        OutEquals = InEquals,
        OutOrder  = InOrder
        ;

        % We should treat use ($<) and ($=) for float attributes 
        % instead of (#<) and (#=)
        #<(AttribA, AttribB, Less),
        #=(AttribA, AttribB, Equals),              

        % InEquals = participants 1 to I-1 are equal
        % OutEquals should extend it up to the I-th participant    
        % OutEquals = InEquals /\ Equals
        ic:and(InEquals, Equals, OutEquals),      

        % InOrder = participants 1 to I-1 are ordered
        % OutOrder should extend it up to the I-th participant
        % OutOrder = InOrder \/ (InEquals /\ Less) 
        ic:and(InEquals, Less, Aux),
        ic:or(InOrder, Aux, OutOrder) )
  ),
  ic:or(AllLess, AllEqual, Result),
  Result #=1.

%------------------------------------------------------------------------------
%
% Associations - multiplicities, uniqueness of links, ...
% 
%------------------------------------------------------------------------------

% constraintsBinAssocMultiplicities(Assoc, RoleA, RoleB, CardList)
%    Define constraints on the participants cardinalities derived from
%    the minimum and maximum  multiplicity of a given association

constraintsBinAssocMultiplicities(Assoc, RoleA, RoleB, CardList) :-
  % Check the value of the "Unique" flag for this association
  assocIsUnique(Assoc, Unique),
  % Get the minimum and maximum cardinalities for both ends
  % of the association
  roleMin(Assoc, RoleA, MinA),
  roleMax(Assoc, RoleA, MaxA),
  roleMin(Assoc, RoleB, MinB),
  roleMax(Assoc, RoleB, MaxB),
  % Get the indices for the associations and both classes
  index(Assoc, AssocIndex),
  roleType(Assoc, RoleA, ClassA),
  index(ClassA, ClassIndexA),
  roleType(Assoc, RoleB, ClassB),
  index(ClassB, ClassIndexB),
  % Get the cardinality variables for the association and both classes
  nth1(AssocIndex, CardList, SizeAssoc),
  nth1(ClassIndexA, CardList, SizeA),
  nth1(ClassIndexB, CardList, SizeB),
  % Multiplicity constraints
  (Unique = 1   -> SizeAssoc #=< SizeA * SizeB; true),
  (MinA  \= 0   -> SizeAssoc #>= MinA * SizeB;  true),
  (MinB  \= 0   -> SizeAssoc #>= MinB * SizeA;  true),
  (MaxA  \= "*" -> SizeAssoc #=< MaxA * SizeB;  true),
  (MaxB  \= "*" -> SizeAssoc #=< MaxB * SizeA;  true).

% constraintsBinAssocMultiplicities(Assoc, RoleA, RoleB, CardList)
%    Define constraints on the participants cardinalities derived from
%    the minimum and maximum  multiplicity of a given association

delay linksConstraintMultiplicities(X,_,_,_) if nonground(X).
linksConstraintMultiplicities(Instances, Assoc, RoleA, RoleB):-
  % Get the minimum and maximum cardinalities for both ends
  % of the association
  roleMin(Assoc, RoleA, MinA),
  roleMax(Assoc, RoleA, MaxA),
  roleMin(Assoc, RoleB, MinB),
  roleMax(Assoc, RoleB, MaxB),
  % Get the indices for roles
  roleIndex(Assoc, RoleA, RoleIndexA),
  roleIndex(Assoc, RoleB, RoleIndexB),
  % Get the indices for the associations and both classes
  index(Assoc, IndexAssoc),
  roleType(Assoc, RoleA, ClassA),
  index(ClassA, ClassIndexA),
  roleType(Assoc, RoleB, ClassB),
  index(ClassB, ClassIndexB),
  % Get the instances variables for the association and both classes
  nth1(ClassIndexA, Instances, OClassA),
  nth1(ClassIndexB, Instances, OClassB),
  nth1(IndexAssoc, Instances, LAssoc),
  getPartList(LAssoc, RoleIndexA, LA),
  getPartList(LAssoc, RoleIndexB, LB),
  ( foreach(Obj, OClassA), 
    param(MinB, MaxB, LA) 
    do
      getOid(Obj, Oid),
      countOidInList(LA, Oid, Size),
      Size #>= MinB, 
      (MaxB  \= "*" -> Size #=< MaxB;  true)
  ),
  ( foreach(Obj2, OClassB), 
    param(MinA, MaxA, LB) 
    do
      getOid(Obj2, Oid2),
      countOidInList(LB, Oid2, Size2),
      Size2 #>= MinA, 
      (MaxA \= "*" -> Size2 #=< MaxA; true)
  ).

% differentLinks(LinkList)
%    All links in an association must have at least a different participant
%    (except for isUnique associations)

differentLinks(LinkList):- 
  differentList(differenceForLinks, LinkList).

% differenceForLinks(LinkA, LinkB) :-
%    Constrain two links to be different: at least one participant must
%    be different

differenceForLinks(LinkA, LinkB) :-
  ( foreacharg(ParticipantA, LinkA),
    foreacharg(ParticipantB, LinkB),
    fromto(0, In, Out, Result)
    do
       % Aux = (ParticipantA <> ParticipantB)
       #\=(ParticipantA, ParticipantB, Aux),
       ic:or(In, Aux, Out)
  ),
  % Result is PartA1 <> PartB1 or PartA2 <> PartB2 or ...
  Result #= 1.

% orderedLinks(LinkList) :-
%    All links of an association must be defined in some order
%    This restriction is imposed for efficiency reasons to avoid
%    exploring all possible permutations of links within an association

orderedLinks(LinkList) :-
   orderedList(orderForLinks, LinkList).

% orderForLinks(LinkA, LinkB) :-
%    Constrain LinkA to be strictly less than LinkB. Let p(i,L) be the i-th 
%    participant of L, then LinkA is less than LinkB if:
%      ( p(1,LA) < p(1,LB) ) OR
%      ( p(1,LA) = p(1,LB) AND p(2,LA) < p(2,LB) ) OR
%      ( p(1,LA) = p(1,LB) AND p(2,LA) = p(2,LB) AND p(3,LA) < p(3,LB) ) OR
%      ...

orderForLinks(LinkA, LinkB) :-
  ( foreacharg(ParticipantA, LinkA), 
    foreacharg(ParticipantB, LinkB),
    fromto(0, InOrder, OutOrder, Result),
    fromto(1, InEquals, OutEquals, _)
    do
      #<(ParticipantA, ParticipantB, Less),
      #=(ParticipantA, ParticipantB, Equals),              

      % InEquals = participants 1 to I-1 are equal
      % OutEquals should extend it up to the I-th participant    
      % OutEquals = InEquals /\ Equals
      ic:and(InEquals, Equals, OutEquals),      

      % InOrder = participants 1 to I-1 are ordered
      % OutOrder should extend it up to the I-th participant
      % OutOrder = InOrder \/ (InEquals /\ Less) 
      ic:and(InEquals, Less, Aux),
      ic:or(InOrder, Aux, OutOrder) 
  ),
  Result #=1.

%------------------------------------------------------------------------------
%
% Inheritance - disjoint, complete, ...
% 
%------------------------------------------------------------------------------

% constraintsSubtypesCard(Super, Subs) :-
%    Cardinality of subtypes cannot be greater than cardinality supertype

constraintsSubtypesCard(Super, Subs):-
  ( foreach(Si, Subs), param(Super) do Super#>=Si ). 

% existsOidIn(OSub, OSuper):-
%    Oids of subtype instances must exist in the list of oids for the supertype

existsOidIn(OSub, OSuper) :-
   getOidList(OSub, OidListSub),
   getOidList(OSuper, OidListSuper),
   ( foreach(Oid, OidListSub),
     param(OidListSuper)
     do
        existsOidInList(Oid, OidListSuper)
   ).

%------------------------------------------------------------------------------
%
% Auxiliary methods
% 
%------------------------------------------------------------------------------

% nth1( N, List, Value) :-
%    Get the value in the n-th position of the list
%    Consider that the first element of the list is in position 1

nth1( _, [], _ ) :- 
   writeln("Internal error"),
   writeln(" Term nth1/3 invoked with empty list"), 
   abort. 
nth1( N, [H|T], X) :-
   ( N > 1 ->
     Aux is N-1,
     nth1( Aux, T, X);
     X = H ).

% orderedList(OrderCriterion, List) :-
%    Check if a List is ordered according to some ordering criterion (e.g. #<),
%    such that ord(X,Y) succeds if X <= Y

orderedList(OrderCriterion, List) :-
   ( List = [] -> true;  
     ( fromto(List, [This,Next|Rest], [Next|Rest], [_]),
       param(OrderCriterion)
       do
          apply(OrderCriterion, [This, Next])
      )
   ).

% differentList(DifferCriterion, List) :-
%    Check if all elements of a List are different, according to some
%    "difference" criterion (e.g. #\=), such that dif(X,Y) succeeds if X<>Y

differentList(DifferCriterion, List) :-
  ( fromto(List, [This|Rest], Rest, []),
    param(DifferCriterion)
    do
      ( foreach(Other,Rest), 
        param(This,DifferCriterion)
        do
          apply(DifferCriterion, [This, Other])
      )
  ).

% getPartList( LinkList, RoleIndex, OidList ) :-
%    Computes the list of participants in a given role of an association
%    The list has as many elements as links in the association

getPartList(LinkList, RoleIndex, OidList) :-
   ( foreach(Link, LinkList),
     foreach(Oid,  OidList),
     param(RoleIndex) 
     do
        arg(RoleIndex, Link, Oid) 
   ). 

%
% ECLiPSe libraries
%
:- lib(ic).      % Interval constraints
:- lib(apply).   % Using variables as functors

% Correctness properties

% strongSatisfiabilityConstraint(?Vars) :-
%    Constrains all cardinality variables in Vars to be strictly greater than 0 

strongSatisfiabilityConstraint(Vars):- 
   ( foreach(Vi,Vars) do Vi#>0 ).

% weakSatisfiabilityConstraint(?Vars) :-
%    Constrains the sum of all cardinality variables in Vars to be strictly 
%    greater than 0 

weakSatisfiabilityConstraint(Vars) :-
   sum(Vars) #> 0.

% livelinessConstraint(?Vars, +Typename):-
%    Constrains the cardinality of a given class to be greater than 0

livelinessConstraint(Vars, Typename) :-
   index(Typename, Index),
   nth1(Index, Vars, Card),
   Card #> 0.

% noConstraintSubsumption(?Instances, +Constraint1, +Constraint2) :-
%    The variables of Instances must be assigned in such a way that
%    Constraint1 is satisfied and Constraint2 is not satisfied

noConstraintSubsumption(Instances, Constraint1, Constraint2) :-
   apply(Constraint1, [Instances, [], TruthValue1]),
   apply(Constraint2, [Instances, [], TruthValue2]),
   TruthValue1 #= 1,
   TruthValue2 #= 0.

% noConstraintRedundancy(?Instances, +Constraint1, +Constraint2) :-
%    The variables of Instances must be assigned in such a way that
%    only Constraint1 or only Constraint2 is satisfied, but not both

noConstraintRedundancy(Instances, Constraint1, Constraint2) :-
   apply(Constraint1, [Instances, [], TruthValue1]),
   apply(Constraint2, [Instances, [], TruthValue2]),
   TruthValue1 #\= TruthValue2.

%
% OCL Standard Library - Predefined Iterators for Collections
% 

% 2007/01/31:
%
% Operations that do not adhere to the standard
% - Collection.collect() does not work properly so far,
%   as it is based on flatten()
% Undefined behaviors in the standard
% - The element returned by Collection.any() is chosen arbitrarily

% 2007/03/20:
% - Fully operational
%   * ocl_col_one, ocl_col_forAll, ocl_col_exists, ocl_col_isUnique, ocl_col_any
%   * ocl_set_select, ocl_set_reject
% - To be fixed
%   * forAll and exists can be implemented with "and" or "or" instead of the
%     sum of N variables. It is not clear whether the efficiency of the method
%     will improve or not
% - Missing operators
%   * collect, collectNested

%
% ECLiPSe libraries
%
:- lib(ic).             % Interval constraints
:- lib(apply).          % Apply predicates to lists
:- lib(apply_macros).   % Predefined applications of predicates 
:- lib(lists).          % Operations on lists

%------------------------------------------------------------------------------
% Collection iterators
%------------------------------------------------------------------------------

% ocl_col_exists(Instances, Vars, Collection, Predicate, Result) :- 
%    Test if Predicate holds in at least one element of Collection
%    Exists is always false on the empty collection

ocl_col_exists(Instances, Vars, Collection, Predicate, Result ) :-
   Result::0..1,
   property_sat_count(Instances, Vars, Collection, Predicate, N),
   #>(N, 0, Result).

% ocl_col_forAll(Instances, Vars, Collection, Predicate, Result) :- 
%    Test if Predicate holds in all elements of Collection

ocl_col_forAll(Instances, Vars, Collection, Predicate, Result ) :-
   Result::0..1,
   property_sat_count(Instances, Vars, Collection, Predicate, N),
   ocl_col_size(Collection, S),
   #=(N, S, Result).

% ocl_col_isUnique(Instances, Vars, Collection, Predicate, Result) :-
%    Test if applying Predicate to Collection produces a list
%    with unique values

ocl_col_isUnique(Instances, Vars, Collection, Predicate, Result ) :-
  Result::0..1,
  property_apply(Instances, Vars, Collection, Predicate, List),  
  list_is_unique(List, Result).
                               
% ocl_col_any(Instances, Vars, Collection, Predicate, Result) :-
%    Result is any element of Collection which satisfies 
%    Predicate.                                       

delay ocl_col_any(_, _, X, _, _) if var(X).
ocl_col_any(_, _, [], _, ocl_undef).
ocl_col_any(Instances, Vars, [H|T], Predicate, Result) :-
  apply( Predicate, [Instances, [H|Vars], Value] ),
  aux_find_first_success( Instances, Vars, [H|T], Predicate, Value, Result ).

delay aux_find_first_success(_, _, _, _, X, _) if var(X).
aux_find_first_success( _, _, [H|_], _, 1, H ).
aux_find_first_success( Instances, Vars, [_|T], Predicate, 0, Result ) :-
  ocl_col_any(Instances, Vars, T, Predicate, Result ).

% ocl_one(Collection, Predicate) :-
%    Test if there is only one element in Collection which
%    satisfies Predicate

ocl_col_one(Instances, Vars, Collection, Predicate, Result ) :-
   property_sat_count(Instances, Vars, Collection, Predicate, N),
   #=(N, 1, Result).
   
% ocl_T_collect(Instances, Vars, Collection, Predicate, Result) :-
%    Result is the Collection of elements produced by applying
%    Predicate to all elements of the collection and flattening
%    them. Behavior depends on the collection type.

ocl_set_collect(Instances, Vars, Set, Predicate, Result) :- 
    ocl_set_collectNested(Instances, Vars, Set, Predicate, X),
    ocl_bag_flatten(X, Result).
ocl_bag_collect(Instances, Vars, Bag, Predicate, Result) :- 
    ocl_bag_collectNested(Instances, Vars, Bag, Predicate, X),
    ocl_bag_flatten(X, Result).
ocl_seq_collect(Instances, Vars, Seq, Predicate, Result) :- 
    ocl_seq_collectNested(Instances, Vars, Seq, Predicate, X),
    ocl_seq_flatten(X, Result).

%------------------------------------------------------------------------------
% Set iterators
%------------------------------------------------------------------------------

% ocl_set_select(Instances, Vars, Set, Predicate, Result) :-
%    Result is the subset of elements in Set that satisfy Predicate

ocl_set_select(Instances, Vars, Set, Predicate, Result) :-
   property_apply(Instances, Vars, Set, Predicate, List),
   aux_col_select(Set, List, Result).

% ocl_set_reject(Instances, Vars, Set, Predicate, Result) :-
%    Result is the subset of elements in Bag that do not satisfy Predicate

ocl_set_reject(Instances, Vars, Set, Predicate, Result) :-
   property_apply(Instances, Vars, Set, Predicate, List),
   aux_col_reject(Set, List, Result).

% ocl_set_collectNested(Instances, Vars, Set, Predicate, Result) :-
%    Result is the set produced by applying Predicate to all elements in 
%    the Set

ocl_set_collectNested(Instances, Vars, Set, Predicate, Result) :- 
   property_apply(Instances, Vars, Set, Predicate, Aux),
   suspend(sort(Aux, Result), 0, Aux->inst).

% ocl_set_sortedBy(Instances, Vars, Set, Predicate, Result) :-
%    Result is the OrderedSet computed by ordering the elements of Set
%    in increasing order according to the values of Predicate

ocl_set_sortedBy(Instances, Vars, Set, Predicate, Result) :- 
   qsort_apply(Instances, Vars, Set, Predicate, Result).

%------------------------------------------------------------------------------
% Bag iterators
%------------------------------------------------------------------------------

% ocl_bag_select(Instances, Vars, Bag, Predicate, Result) :-
%    Result is the subbag of elements in Bag that satisfy Predicate

ocl_bag_select(Instances, Vars, Bag, Predicate, Result) :-
   property_apply(Instances, Vars, Bag, Predicate, List),
   aux_col_select(Bag, List, Result).

% ocl_bag_reject(Instances, Vars, Bag, Predicate, Result) :-
%    Result is the subbag of elements in Bag that do not satisfy Predicate

ocl_bag_reject(Instances, Vars, Bag, Predicate, Result) :-
   property_apply(Instances, Vars, Bag, Predicate, List),
   aux_col_reject(Bag, List, Result).

% ocl_bag_collectNested(Instances, Vars, Bag, Predicate, Result) :-
%    Result is the bag produced by applying Predicate to all elements in 
%    the Bag

ocl_bag_collectNested(Instances, Vars, Bag, Predicate, Result) :- 
   property_apply(Instances, Vars, Bag, Predicate, Result).

% ocl_bag_sortedBy(Instances, Vars, Bag, Predicate, Result) :-
%    Result is the Sequence computed by ordering the elements of Bag
%    in increasing order according to the values of Predicate

ocl_bag_sortedBy(Instances, Vars, Bag, Predicate, Result) :- 
   qsort_apply(Instances, Vars, Bag, Predicate, Result).

%------------------------------------------------------------------------------
% Sequence iterators
%------------------------------------------------------------------------------

% ocl_seq_select(Instances, Vars, Seq, Predicate, Result) :-
%    Result is the subsequence of elements in Seq that satisfy Predicate
%    The relative order among elements should be preserved.

ocl_seq_select(Instances, Vars, Seq, Predicate, Result) :-
   property_apply(Instances, Vars, Seq, Predicate, List),
   aux_col_select(Seq, List, Result).

% ocl_seq_reject(Instances, Vars, Seq, Predicate, Result) :-
%    Result is the subsequence of elements in Seq that do not satisfy 
%    Predicate.
%    The relative order among elements should be preserved.

ocl_seq_reject(Instances, Vars, Seq, Predicate, Result) :-
   property_apply(Instances, Vars, Seq, Predicate, List),
   aux_col_reject(Seq, List, Result).

% ocl_seq_collectNested(Seq, Predicate, Result) :-
%    Result is the sequence produced by applying Predicate to all 
%    elements in Seq

ocl_seq_collectNested(Instances, Vars, Seq, Predicate, Result) :- 
   property_apply(Instances, Vars, Seq, Predicate, Result).

% ocl_seq_sortedBy(Seq, Predicate, Result) :-
%    Result is the Sequence computed by ordering the elements of Seq
%    in increasing order according to the values of Predicate

ocl_seq_sortedBy(Instances, Vars, Seq, Predicate, Result) :- 
   qsort_apply(Instances, Vars, Seq, Predicate, Result).

%------------------------------------------------------------------------------
% Auxiliary predicates
%------------------------------------------------------------------------------

% property_apply(Instances, Vars, Collection, Property, Result) :-
%    Compute the list produced by applying the property to
%    all elements of the collection. The list appears in the same
%    order as the elements in the original set.

delay property_apply(_,_,X,_,_) if var(X).
property_apply(Instances, Vars, Collection, Property, Result) :- 
   ( 
     foreach(Elem, Collection),   
     foreach(Value, Result),
     param(Property, Instances, Vars)
     do
       apply(Property, [Instances, [Elem|Vars], Value]) 
   ). 
   
% property_sat_count(Instances, Vars, Collection, Property, Result) :-
%    Count the number of elements in the collection that satisfy
%    a given Property.

delay property_sat_count(_, _, X, _, _) if var(X).
property_sat_count(Instances, Vars, Collection, Property, Result ) :- 
   property_apply(Instances, Vars, Collection, Property, TruthValues),
   Result #= sum(TruthValues). 

% aux_col_select(Collection, List, Result) :-
%    Result is the subset of elements in the Collection where
%    the same element in the List is true

delay aux_col_select(X, _, _) if var(X).
delay aux_col_select(_, Y, _) if nonground(Y).
aux_col_select(Collection, List, Result) :-
  ( foreach(Elem,Collection),
    foreach(TruthValue,List),
    fromto(Result,In,Out,[])
    do
      ( TruthValue = 1 -> In = [Elem | Out] ; In = Out ) 
  ). 

% aux_col_reject(Collection, List, Result) :-
%    Result is the subset of elements in the Collection where
%    the same element in the List is false

delay aux_col_reject(X, _, _) if var(X).
delay aux_col_reject(_, Y, _) if nonground(Y).
aux_col_reject(Collection, List, Result) :-
  ( foreach(Elem,Collection),
    foreach(TruthValue,List),
    fromto(Result,In,Out,[])
    do
      ( TruthValue = 0 -> In = [Elem | Out] ; In = Out ) 
  ). 

% list_is_unique(List, Result) :-
%    Result is true if and only if the list does not have repeated
%    elements

delay list_is_unique(X, _) if nonground(X).
list_is_unique([], 1).
list_is_unique([H|T], X) :- (member(H,T) -> X = 0 ; list_is_unique(T,X)). 

% qsort_apply(Instances, Vars, List, Pred, Out) :-
%    Out is the sorted version of List. Elements are sorted in increasing
%    order according to the result of Predicate applied to each element.

qsort_apply(_, _, [], _, []).
qsort_apply(Instances, Vars,[H|T], Predicate, Y) :-
   part_apply(Instances, Vars, H, T, Predicate, Smaller, Larger),
   qsort_apply(Instances, Vars, Smaller, Predicate, S),
   qsort_apply(Instances, Vars, Larger, Predicate, L),
   append(S, [H|L], Y).

% part_apply(Instances, Vars, Elem, Rest, Pred, Smaller, Larger) :-
%    Partition the list Rest into two sublists, Smaller and Larger, having all
%    elements which are respectively <= and > in the order wrt Elem. The
%    order is based on the result of applying Pred to the elements of Rest.

part_apply(_, _, _, [], _, [], []).
part_apply(Instances, Vars, X, [Y|Xs], Pred, [Y|Ls],Bs) :-
    apply(Pred, [Instances, [X|Vars], S]),
    apply(Pred, [Instances, [Y|Vars], T]),
    S > T,
    part_apply(Instances, Vars, X, Xs, Pred, Ls, Bs).
part_apply(Instances, Vars, X, [Y|Xs], Pred, Ls, [Y|Bs]) :-
    apply(Pred, [Instances, [X|Vars], S]),
    apply(Pred, [Instances, [Y|Vars], T]),
    S =< T,
    part_apply(Instances, Vars, X, Xs, Pred, Ls, Bs).


%
% OCL Standard Library - Collection classes 
% 
% Implemented classes:
% - Collection  
% - Set
% - Bag
% - Sequence
% - OrderedSet

% 2007/03/29:
%
% Operations that do not adhere to the standard
% - flatten() and sum() do not work properly so far because they
%   require knowing the type of the elements of the collection
%
% Incorrect behavior in the standard
% - The post of OrderedSet.append(), OrderedSet.prepend() and 
%   OrderedSet.insertAt() is incorrect as it does not guarantee
%   the absence of duplicates after the insertion 
%
% Undefined behaviors in the standard
% - Order of the elements in the collection returned by asSequence()
% - Behavior of Sequence.inserAt() and OrderedSet.insertAt() if the index is 
%   outside bounds
% - Behavior of Sequence.indexOf() if the object does not appear in 
%   the sequence or it appears multiple times (the position being returned 
%   is not specified)
% - Behavior of first() and last() in empty Sequences and OrderedSets

%
% ECLiPSe libraries
%
:- lib(ic).       % Interval constraints
:- lib(lists).    % List manipulation
:- lib(ordset).   % Ordered set manipulation

%------------------------------------------------------------------------------
%
% Collection - A generic collection of elements backed by a Prolog list
% 
%------------------------------------------------------------------------------

% ocl_col_size( +Col, -Size ) :-
%    Returns the number of elements in the collection

delay ocl_col_size(X, _) if var(X).
ocl_col_size(Col, Size) :- 
  length(Col, Size).

% ocl_col_includes( +Col, +Obj, -Result ) :-
%    Tests if object Obj is inside Col. In that case, 
%    Result = 1 if Obj is in Col, 0 otherwise.

delay ocl_col_includes(X, _, _) if nonground(X).
delay ocl_col_includes(_, Y, _) if nonground(Y).
ocl_col_includes(Col, Obj, Result) :- 
   (member(Obj, Col) -> Result = 1; Result = 0).  
  
% ocl_col_excludes( +Col, +Obj, -Result ) :- 
%    Tests if object Obj is inside Col. In that case, 
%    Result = 1 if Obj is in Col, 1 otherwise.

ocl_col_excludes(Col, Obj, Result) :-
   Result::0..1,
   ocl_col_includes(Col, Obj, Aux),
   ic:neg(Aux, Result).

% ocl_col_count( +Col, +Obj, -Result ) :-
%    Result is the number of instances of Obj within Col

delay ocl_col_count(X, _, _) if nonground(X).
delay ocl_col_count(_, Y, _) if nonground(Y).
ocl_col_count( Col, Obj, Result ) :-
  Result::0..1,
  ( foreach(Elem, Col),
    fromto(0, In, Out, Result),
    param(Obj) 
    do
      ( Elem = Obj -> Out is In + 1; Out is In )
  ).

% ocl_col_includesAll( +Col1, +Col2, -Result ) :- 
%    Result is 1 if Col1 includes all elements of Col2
%    and 0 otherwise

delay ocl_col_includesAll(X, _, _) if nonground(X).
delay ocl_col_includesAll(_, Y, _) if nonground(Y).
ocl_col_includesAll(Col1, Col2, Result) :-
   ( Col2 = [] -> 
     Result = 1; 
     sort(Col1, OrderedCol1),
     sort(Col2, OrderedCol2),
     ( subset(OrderedCol2, OrderedCol1) ->
       Result = 1;
       Result = 0 
     )
   ).   

% ocl_col_excludesAll( +Col1, +Col2, -Result) :-
%    Result is 1 if Col1 does not include any element of Col2
%    and 0 otherwise

delay ocl_col_excludesAll(X, _, _) if nonground(X).
delay ocl_col_excludesAll(_, Y, _) if nonground(Y).
ocl_col_excludesAll(Col1, Col2, Result) :-
   ( Col2 = [] ->
     Result = 1;
     ( Col1 = [] ->
       Result = 1;
       list_to_ord_set(Col1, OrderedCol1),
       list_to_ord_set(Col2, OrderedCol2),
       ( ord_intersect(OrderedCol1, OrderedCol2) ->
         Result = 0;
         Result = 1 
       )
     ) 
   ). 

% ocl_col_isEmpty( +Col, -Result ) :-
%    Result is 1 if the collection is empty, 0 otherwise

delay ocl_col_isEmpty(X, _) if var(X).
ocl_col_isEmpty([], 1) :- !.
ocl_col_isEmpty([_|_], 0) :- !.

% ocl_col_notEmpty( +Col, -Result ) :-
%    Result is 1 if the collection is not empty, 0 otherwise

delay ocl_col_notEmpty(X, _) if var(X).
ocl_col_notEmpty([], 0) :- !.
ocl_col_notEmpty([_|_], 1) :- !.

% ocl_col_sum( ?Col, ?Result ) :-
%    Result is the sum of all elements within the collection
%    Warning: currently this method only works properly for
%    collections of integers

delay ocl_col_sum(X, _) if var(X).
ocl_col_sum(Col, Result) :- Result #= sum(Col).
                                          
% ocl_col_product( +Col1, +Col2, +Result ) :- 
%    Result is a set with the cartesian product of the elements
%    of two collections. The result should be a set, so duplicates 
%    should be removed

delay ocl_col_product(X, _, _) if nonground(X).
delay ocl_col_product(X, _, _) if nonground(X).
ocl_col_product([], _, []) :- !.
ocl_col_product(_, [], []) :- !.
ocl_col_product([First1|Rest1], [First2|Rest2], Result) :-
                cartesian_product(First1, [First2|Rest2], Aux1),
                ocl_col_product(Rest1, [First2|Rest2], Aux2),
                append(Aux1, Aux2, Aux3),
                sort(Aux3, Result).

% cartesian_product(X,Y,Z) 
%    Combine X with each element of list Y
%    The result will be stored in the list Z

cartesian_product(Obj, Col, Result) :-
   ( foreach(Elem, Col),
     foreach([Obj, Elem], Result),
     param(Obj)
     do 
        true
   ).
                                  
%------------------------------------------------------------------------------
%
% Set - A set (unordered collection of elements without duplicates). 
%
%------------------------------------------------------------------------------

% Operations inherited from collection
ocl_set_size(Set, Size)               :- ocl_col_size(Set, Size).
ocl_set_includes(Set, Obj, Result)    :- ocl_col_includes(Set, Obj, Result).
ocl_set_excludes(Set, Obj, Result)    :- ocl_col_excludes(Set, Obj, Result).
ocl_set_count(Set, Obj, N)            :- ocl_col_count(Set, Obj, N).
ocl_set_includesAll(Set, Col, Result) :- ocl_col_includesAll(Set, Col, Result).
ocl_set_excludesAll(Set, Col, Result) :- ocl_col_excludesAll(Set, Col, Result).
ocl_set_isEmpty(Set, Result)          :- ocl_col_isEmpty(Set, Result).
ocl_set_notEmpty(Set, Result)         :- ocl_col_notEmpty(Set, Result).
ocl_set_sum(Set, N)                   :- ocl_col_sum(Set, N).
ocl_set_product(Set, Col, Product)    :- ocl_col_product(Set, Col, Product). 

% ocl_set_including( +Set, +Obj, -Result ) :-
%    Add Obj to Set if it was not already there, Result stores the new set

delay ocl_set_including(X, _, _) if nonground(X).
delay ocl_set_including(_, Y, _) if nonground(Y).
ocl_set_including(Set, Obj, Result) :-
   list_to_ord_set(Set, Aux),
   ord_insert(Aux, Obj, Result).

% ocl_set_union( +Set1, +Set2, -Result) :- 
%    Result is the union of Set1 and Set2    

delay ocl_set_unionSet(X, _, _) if nonground(X).
delay ocl_set_unionSet(_, Y, _) if nonground(Y).
ocl_set_unionSet(Set1, Set2, Result) :- 
   list_to_ord_set(Set1, Aux1),
   list_to_ord_set(Set2, Aux2),
   ord_union(Aux1, Aux2, Result).

% ocl_set_union( +Set, +Bag, -Result ) :-
%    Result is the union of Set and Bag
%    A Bag can hold multiple copies of the same element

delay ocl_set_unionBag(X, _, _) if nonground(X).
delay ocl_set_unionBag(_, Y, _) if nonground(Y).
ocl_set_unionBag(Set, Bag, Result) :-
   list_to_ord_set(Set, Aux1),
   list_to_ord_set(Bag, Aux2),    
   ord_union(Aux1, Aux2, Result).  

% ocl_set_equals( +Set1, +Set2, -Result ) :- 
%    Result is true if Set1 = Set2

delay ocl_set_equals(X, _, _) if nonground(X).
delay ocl_set_equals(_, Y, _) if nonground(Y).
ocl_set_equals(Set1, Set2, Result) :- 
   list_to_ord_set(Set1, Aux1),
   list_to_ord_set(Set2, Aux2),
   ( Aux1 = Aux2 -> Result = 1; Result = 0 ).

% ocl_set_intersection( +Set1, +Set2, -Result ) :- 
%    Result is the intersection of Set1 and Set2

delay ocl_set_intersectionSet(X, _, _) if nonground(X).
delay ocl_set_intersectionSet(_, Y, _) if nonground(Y).
ocl_set_intersectionSet(Set1, Set2, Result) :- 
   list_to_ord_set(Set1, Aux1),
   list_to_ord_set(Set2, Aux2),
   ord_intersection(Aux1, Aux2, Result).

% ocl_set_intersection( +Set1, +Bag, -Result ) :-
%    Result is the intersection of Set and Bag
%    A Bag can hold multiple copies of the same element

delay ocl_set_intersectionBag(X, _, _) if nonground(X).
delay ocl_set_intersectionBag(_, Y, _) if nonground(Y).
ocl_set_intersectionBag(Set, Bag, Result) :- 
   list_to_ord_set(Set, Aux1),
   list_to_ord_set(Bag, Aux2),
   ord_intersection(Aux1, Aux2, Result).  

% ocl_set_difference( +Set1, +Set2, -Result ) :- 
%    Result is Set1 - Set2

delay ocl_set_difference(X, _, _) if nonground(X).
delay ocl_set_difference(_, Y, _) if nonground(Y).
ocl_set_difference(Set1, Set2, Result):- 
   list_to_ord_set(Set1, Aux1),
   list_to_ord_set(Set2, Aux2),
   ord_subtract(Aux1, Aux2, Result).
    
% ocl_set_excluding( +Set, +Obj, -Result ) :-
%    Result = Set - Obj

delay ocl_set_excluding(X, _, _) if nonground(X).
delay ocl_set_excluding(_, Y, _) if nonground(Y).
ocl_set_excluding(Set, Obj, Result ):- 
   list_to_ord_set(Set, Aux),
   ord_del_element(Aux, Obj, Result).

% ocl_set_symmetricDifference( +Set1, +Set2, -Result ) :- 
%    Result holds the elements in Set1 and Set2 but not in both

delay ocl_set_symmetricDifference(X, _, _) if nonground(X).
delay ocl_set_symmetricDifference(_, Y, _) if nonground(Y).
ocl_set_symmetricDifference(Set1, Set2, Result) :-
   list_to_ord_set(Set1, Aux1),
   list_to_ord_set(Set2, Aux2),
   ord_symdiff(Aux1, Aux2, Result). 

% ocl_set_flatten( +Set, -Result ) :- 
%    Flattens the elements in SET if they are collections
%
% WARNING: this operation always flattens the elements in the list. If the list
% holds other types of data that are stored as Prolog lists, the results of 
% these operations are impredictable.

delay ocl_flatten(X, _) if nonground(X).
ocl_set_flatten(Set, Result) :- 
   flatten(Set, Result).

% ocl_set_asSet( +Set, -Result ) :- 
%    Returns the set itself

ocl_set_asSet(Set, Set) :- !.

% ocl_set_asOrderedSet( +Set, -Result ) :- 
%    Return the set, ordering all elements.

delay ocl_set_asOrderedSet(X, _) if nonground(X).
ocl_set_asOrderedSet(Set, Result) :- sort(Set, Result).

% ocl_set_asSequence( +Set, -Result ) :- 
%    Return a Sequence view of the set
%    The order of elements is not specified

ocl_set_asSequence(Set, Set) :- !.

% ocl_set_asBag( +Set, -Result ) :- 
%     Return a Bag view of the set

ocl_set_asBag(Set, Set) :- !.

%------------------------------------------------------------------------------
%
% Bag - A multiset (an unordered collection with potential duplicates).
%
%------------------------------------------------------------------------------

% Operations inherited from collection
ocl_bag_size(Bag, Size)               :- ocl_col_size(Bag, Size).
ocl_bag_includes(Bag, Obj, Result)    :- ocl_col_includes(Bag, Obj, Result).
ocl_bag_excludes(Bag, Obj, Result)    :- ocl_col_excludes(Bag, Obj, Result).
ocl_bag_count(Bag, Obj, N)            :- ocl_col_count(Bag, Obj, N).
ocl_bag_includesAll(Bag, Col, Result) :- ocl_col_includesAll(Bag, Col, Result).
ocl_bag_excludesAll(Bag, Col, Result) :- ocl_col_excludesAll(Bag, Col, Result).
ocl_bag_isEmpty(Bag, Result)          :- ocl_col_isEmpty(Bag, Result).
ocl_bag_notEmpty(Bag, Result)         :- ocl_col_notEmpty(Bag, Result).
ocl_bag_sum(Bag, N)                   :- ocl_col_sum(Bag, N).
ocl_bag_product(Bag, Col, Product)    :- ocl_col_product(Bag, Col, Product). 

% ocl_bag_equals( +Bag1, +Bag2, -Result ) :- 
%    Result is 1 if both bags hold the same set of elements and
%    each element appears the same number of times, 0 otherwise

delay ocl_bag_equals(X, _, _) if nonground(X).
delay ocl_bag_equals(_, Y, _) if nonground(Y).
ocl_bag_equals([], []) :- !.
ocl_bag_equals([First1|Rest1],[First2|Rest2]) :-
   msort([First1|Rest1], Aux1),
   msort([First2|Rest2], Aux2),
   Aux1 = Aux2.
       
% ocl_bag_union( +Bag1, +Bag2, -Result ) :-
%    Result = Bag1 union Bag2

delay ocl_bag_unionBag(X, _, _) if nonground(X).
delay ocl_bag_unionBag(_, Y, _) if nonground(Y).
ocl_bag_unionBag(Bag1, Bag2, Result) :- 
    append(Bag1, Bag2, Result).
       
% ocl_bag_union( +Bag, +Set, -Result ) :- 
%    Result = Bag union Set

delay ocl_bag_unionSet(X, _, _) if nonground(X).
delay ocl_bag_unionSet(_, Y, _) if nonground(Y).  
ocl_bag_unionSet(Bag, Set, Result) :- 
       append(Bag, Set, Result).
       
% ocl_bag_intersection( +Bag1, +Bag2, -Result ) :- 
%    Result is the intersection of Bag1 and Bag2 

delay ocl_bag_intersectionBag(X, _, _) if nonground(X).
delay ocl_bag_intersectionBag(_, Y, _) if nonground(Y).  
ocl_bag_intersectionBag(Bag1, Bag2, Result) :-
       msort(Bag1, SortedBag1),
       msort(Bag2, SortedBag2),
       intersect_with_duplicates(SortedBag1, SortedBag2, Result).              
              
% intersect_with_duplicates( +X, +Y, -Z ) :- 
%    X and Y are ordered lists, possibly with duplicates. Z should contain 
%    all elements that appear in both lists, as many times as the minimum
%    number of appearances of the element in X and Y

intersect_with_duplicates([], _, []) :- !.
intersect_with_duplicates(_, [], []) :- !.
intersect_with_duplicates([X|Rest1], [X|Rest2], Result) :-
       intersect_with_duplicates(Rest1, Rest2, Aux),
       Result is [X|Aux].
intersect_with_duplicates([First1|Rest1], [First2|Rest2], Result) :-
       First1 @< First2, !,
       intersect_with_duplicates(Rest1, [First2|Rest2], Result).
intersect_with_duplicates([First1|Rest1], [First2|Rest2], Result) :-
       First1 @> First2, !,
       intersect_with_duplicates([First1|Rest1], Rest2, Result).
       
% ocl_bag_intersection( +Bag, +Set, -Result ) :- 
%    Result = Bag intersection Set
%    No "delay" are required for this predicate, as the operation
%    is just a proxy towards ocl_set_interesectionBag/3.

ocl_bag_intersectionSet(Bag, Set, Result) :-
   ocl_set_intersectionBag(Bag, Set, Result).
      
% ocl_bag_including( +Bag, +Obj, -Result ) :- 
%    Result is the bag that holds all the elements of Bag plus Obj 
%    No "delay" are required for this predicate.

ocl_bag_including(Bag, Obj, [Obj | Bag]) :- !.

% ocl_bag_excluding( +Bag, +Obj, -Result ) :-
%    Result is a bag with all elements from Bag except Result

delay ocl_bag_excluding(X, _, _) if nonground(X).
delay ocl_bag_excluding(_, Y, _) if nonground(Y).
ocl_bag_excluding([], _, []) :- !.
ocl_bag_excluding([Obj|Rest], Obj, Result) :-        
       ocl_bag_excluding(Rest, Obj, Result).
ocl_bag_excluding([First|Rest], Obj, Result) :-        
       First \== Obj, !,
       ocl_bag_excluding(Rest, Obj, Aux),
       Result is [First|Aux].
       
% ocl_bag_flatten( +Bag, -Result ) :- 
%    Flattens the elements in BAG if they are collections
%
% WARNING: this operation always flattens the elements in the list. If the list
% holds other types of data that are stored as Prolog lists, the results of 
% these operations are impredictable.

delay ocl_bag_flattens(X,_) if nonground(X).
ocl_bag_flattens(Bag, Result) :- 
   flatten(Bag, Result). 
       
% ocl_bag_asSet( +Bag, -Result ) :- 
%    Returns a Set view of the Bag, removing duplicates

delay ocl_bag_asSet(X, _) if nonground(X).
ocl_bag_asSet(Bag, Result) :- sort(Bag, Result).

% ocl_bag_asOrderedSet( +Bag, -Result ) :- 
%    Return a Bag view

ocl_bag_asOrderedSet(Bag, Result) :- sort(Bag, Result).

% ocl_bag_asSequence( +Bag, -Result ) :- 
%    Return a Sequence view of the bag
%    The order of elements is not specified

ocl_bag_asSequence(Bag, Bag) :- !.

% ocl_bag_asBag( +Bag, -Result ) :- 
%    Return the Bag itself

ocl_bag_asBag(Bag, Bag) :- !. 
      
       
%------------------------------------------------------------------------------
%
% Sequence - A sequential collection with random access and
%            potential duplicates.
%
%------------------------------------------------------------------------------

% Operations inherited from collection
ocl_seq_size(Seq, Size)               :- ocl_col_size(Seq, Size).
ocl_seq_includes(Seq, Obj, Result)    :- ocl_col_includes(Seq, Obj, Result).
ocl_seq_excludes(Seq, Obj, Result)    :- ocl_col_excludes(Seq, Obj, Result).
ocl_seq_count(Seq, Obj, N)            :- ocl_col_count(Seq, Obj, N).
ocl_seq_includesAll(Seq, Col, Result) :- ocl_col_includesAll(Seq, Col, Result).
ocl_seq_excludesAll(Seq, Col, Result) :- ocl_col_excludesAll(Seq, Col, Result).
ocl_seq_isEmpty(Seq, Result)          :- ocl_col_isEmpty(Seq, Result).
ocl_seq_notEmpty(Seq, Result)         :- ocl_col_notEmpty(Seq, Result).
ocl_seq_sum(Seq, N)                   :- ocl_col_sum(Seq, N).
ocl_seq_product(Seq, Col, Product)    :- ocl_col_product(Seq, Col, Product).        

% ocl_seq_equals( +Seq1, +Seq2, -Result ) :-
%    Result is 1 if Seq1 and Seq2 are equal (same elements and same order)
%    and 0 otherwise

delay ocl_seq_equals(X, _, _) if nonground(X).
delay ocl_seq_equals(_, Y, _) if nonground(Y).
ocl_seq_equals(Seq1, Seq2, Result) :- 
   ( Seq1 = Seq2 -> Result = 1; Result = 0).
 
% ocl_seq_union( +Seq1, +Seq2, -Result ) :-
%    Result is the sequence formed by all the elements of Seq1 followed by
%    the elements of Seqs

delay ocl_seq_union(X, _, _) if var(X).
delay ocl_seq_union(_, Y, _) if var(Y).
ocl_seq_union(Seq1, Seq2, Result) :- 
   append(Seq1, Seq2, Result).

% ocl_seq_flatten( +Seq, -Result ) :- 
%    Flattens the elements in Seq if they are collections
%
% WARNING: this operation always flattens the elements in the list. If the list
% holds other types of data that are stored as Prolog lists, the results of 
% these operations are impredictable.

delay ocl_seq_flattens(X, _) if nonground(X).
ocl_seq_flattens(Seq, Result) :- 
   flatten(Seq, Result). 

% ocl_seq_append( +Seq, +Obj, -Result ) :- 
%    Result is the sequence computed by adding Obj at the end of Seq

delay ocl_seq_flattens(X, _, _) if var(X).
ocl_seq_append(Seq, Obj, Result) :- 
   append( Seq, [Obj], Result ).

% ocl_seq_prepend( +Seq, +Obj, -Result ) :- 
%    Result is the sequence computed by adding Obj at the beginning of Seq

delay ocl_seq_prepend(X, _, _) if var(X).
ocl_seq_prepend(Seq, Obj, Result) :- 
   Result = [Obj|Seq].

% ocl_seq_insertAt( +Seq, +Obj, +Idx, -Result ) :- 
%    Result is the sequence computed by inserting Obj into Seq in position Idx
%    The behavior of this operation is not specified if the index Idx does not exist
%    exist in the sequence. ASSUMPTION: if Idx is larger than the size of the list
%    then the element is inserted at the end of the list.

delay ocl_seq_insertAt(X, _, _, _) if var(X).
delay ocl_seq_insertAt(_, _, Y, _) if nonground(Y).
ocl_seq_insertAt([], Obj, _, Result)  :- Result = [Obj], !.
ocl_seq_insertAt(Seq, Obj, 1, Result) :- Result = [Obj|Seq], !.
ocl_seq_insertAt([First|Rest],Obj,X,Result) :-
       X > 1, !,
       N is X - 1,
       ocl_seq_insertAt(Rest, Obj, N, Aux),
       Result = [First|Aux].

% ocl_seq_subSequence( +Seq, +Lower, +Upper, -Result ) :- 
%    Result is the subsequence formed by the elemnents of Seq in positions between
%    Lower and Upper. According to the precondition 1 <= Lower <= Upper <= size(Seq)

delay ocl_seq_subSequence(X, _, _, _) if var(X).
delay ocl_seq_subSequence(_, Y, _, _) if nonground(Y).
delay ocl_seq_subSequence(_, _, Z, _) if nonground(Z).
ocl_seq_subSequence(Seq, X, X, Result) :-   
       !,
       nth1(X, Seq, Aux),
       Result = [Aux].
ocl_seq_subSequence(Seq, Lower, Upper, Result) :-
       Lower < Upper, !,
       N is Lower + 1,
       ocl_seq_subSequence(Seq, N, Upper, AuxList),
       nth1(Lower, Seq, AuxElem),
       Result = [AuxElem|AuxList].               
%Alternative implementation (to be tested)
%ocl_seq_subSequence(Seq, Lower, Upper, Result)
%   % Remove the elements after Upper
%   ( foreach(Elem, Seq),
%     foreach(Elem, AuxList),
%     count(_, 1, Upper) do true 
%   ),
%   % Remove the elements before Lower
%   ( Lower = 1 -> 
%     Result = AuxList;
%     ( fromto(AuxList, [First|Rest], Rest, Result),
%       count(_, 1, Lower) do true 
%     )
%   ).
   

% ocl_seq_ at( +Seq, +Idx, -Result ) :- 
%    Result is the element within Seq in position Idx

delay ocl_seq_at(X, _, _) if var(X).
delay ocl_seq_at(_, Y, _) if nonground(Y).
ocl_seq_at(Seq, Idx, Result) :- 
   nth1(Idx, Seq, Result).

% ocl_seq_indexOf( +Seq, +Obj, -Result ) :- 
%    Return a position in Seq that contains Obj
%    The exact position being returned is undefined (we will return the 
%    first). If the object is not found, the behavior is also undefined 

delay ocl_seq_indexOf(X, _, _) if nonground(X).
delay ocl_seq_indexOf(_, Y, _) if nonground(Y).
ocl_seq_indexOf( [], _, _ ) :- fail.
ocl_seq_indexOf( [First|_], First, 1) :- !.
ocl_seq_indexOf( [First|Rest], Obj, Result) :- 
       First \= Obj, !,
       ocl_seq_indexOf( Rest, Obj, N ),
       Result is N + 1.
                
% ocl_seq_first( +Seq, -Result ) :- 
%    Return the first element in the sequence SEQ
%    Behavior is not specified if the sequence is empty

delay ocl_seq_first(X, _) if var(X).
ocl_seq_first([], _) :- fail.
ocl_seq_first([X|_], X) :- !.

% ocl_seq_last( +Seq, -Result ) :- 
%    Return the last element in the sequence SEQ
%    Behavior is not specified if the sequence is empty

delay ocl_seq_last(X, _) if var(X).
ocl_seq_last([], _ ) :- fail.
ocl_seq_last([First|Rest], Result) :-
       length([First|Rest], N),
       nth1([First|Rest], N, Result).
       
% ocl_seq_including( +Seq, +Obj, -Result ) :- 
%   Result is the sequence computed by adding Obj at the end of Seq
%   This operation is equivalent to append()

ocl_seq_including(Seq, Obj, Result) :- 
   ocl_seq_append(Seq, Obj, Result).

% ocl_seq_excluding( +Seq, +Obj, -Result ) :- 
%    Remove all instances of Obj within Seq
%    This operation is equivalent to Bag.excluding

ocl_seq_excluding(Seq, Obj, Result) :- 
   ocl_bag_excluding(Seq, Obj, Result).
       
% ocl_seq_asSet( +Seq, -Result ) :- 
%    Return a Set view of this sequence

delay ocl_seq_asSet(X, _) if nonground(X).
ocl_seq_asSet(Seq, Result) :- 
   list_to_ord_set(Seq, Result).

% ocl_seq_asSequence( +Seq, -Result ) :- 
%    Return the same sequence
ocl_seq_asSequence(Seq, Seq) :- !.

% ocl_seq_asBag( +Seq, -Result ) :- 
%    Return a Bag view of this sequence

ocl_seq_asBag(Seq, Seq) :- !.

% ocl_seq_asOrderedSet( +Seq, -Result ) :- 
%    Return an OrderdedSet view of this sequence by removing duplicates 
%    and keeping the relative order among the remaining elements

delay ocl_seq_asOrderedSet(X, _) if nonground(X).
ocl_seq_asOrderedSet([], []) :- !.
ocl_seq_asOrderedSet([First|Rest],Result) :-
   ocl_seq_asOrderedSet(Rest, Aux),
   ( ocl_seq_includes(Rest, First) ->
     Result = Aux; 
     Result = [First|Aux] 
   ).

%------------------------------------------------------------------------------
%
% OrderedSet - A sequence without duplicates.
%
%------------------------------------------------------------------------------

% Operations inherited from collection
ocl_ordset_size(Set, Size)            :- ocl_col_size(Set, Size).
ocl_ordset_includes(Set, Obj)         :- ocl_col_includes(Set, Obj).
ocl_ordset_excludes(Set, Obj)         :- ocl_col_excludes(Set, Obj).
ocl_ordset_count(Set, Obj, N)         :- ocl_col_count(Set, Obj, N).
ocl_ordset_includesAll(Set, Col, Result) :- 
                                      ocl_col_includesAll(Set, Col, Result).
ocl_ordset_excludesAll(Set, Col, Result) :- 
                                      ocl_col_excludesAll(Set, Col, Result).
ocl_ordset_isEmpty(Set, Result)       :- ocl_col_isEmpty(Set, Result).
ocl_ordset_notEmpty(Set, Result)      :- ocl_col_notEmpty(Set, Result).
ocl_ordset_sum(Set, N)                :- ocl_col_sum(Set, N).
ocl_ordset_product(Set, Col, Product) :- ocl_col_product(Set, Col, Product).

% ocl_ordset_append( +Ordset, +Obj, -Result) :- 
%    If Obj is not in Ordset, Result has all the elements of OrdSet plus Obj
%    at the end. Otherwise, Result is equal to OrdSet

delay ocl_ordset_append(X,_,_) if nonground(X).
delay ocl_ordset_append(_,Y,_) if nonground(Y).
ocl_ordset_append(OrdSet, Obj, Result) :- 
   ( ocl_ordset_includes(OrdSet, Obj, 1) ->
     Result = OrdSet;
     append(OrdSet, [Obj], Result)
   ).

% ocl_ordset_prepend( +OrdSet, +Obj, -Result ) :- 
%    If Obj is not in Ordset, Result has all the elements of OrdSet plus Obj
%    at the beginning. Otherwise, Result is equal to OrdSet

delay ocl_ordset_prepend(X,_,_) if nonground(X).
delay ocl_ordset_prepend(_,Y,_) if nonground(Y).
ocl_ordset_prepend(OrdSet, Obj, Result) :- 
   ( ocl_ordset_includes(OrdSet, Obj, 1) ->
     Result = OrdSet;
     Result = [Obj|OrdSet]
   ).
            
% ocl_ordset_insertAt( +OrdSet, +Obj, +Idx, -Result) :- 
%    If Obj is in OrdSet, Result is equal to OrdSet
%    Otherwise, Result is computed by inserting Obj in position Idx of OrdSet

delay ocl_ordset_insertAt(X, _, _, _) if nonground(X).
delay ocl_ordset_insertAt(_, Y, _, _) if nonground(Y).
delay ocl_ordset_insertAt(_, _, Z, _) if nonground(Z).
ocl_ordset_insertAt(OrdSet, Obj, Idx, Result) :-
   ( ocl_ordset_inclues(OrdSet, Obj, 1) ->
     Result = OrdSet;
     ocl_seq_insertAt(OrdSet, Obj, Idx, Result)
   ).

% ocl_ordset_subOrderedSet( +OrdSet, +Lower, +Upper, -Result ) :-
%    Returns the subset between positions Lower and Upper within the set
%    According to the precondition 1 <= Lower <= Upper <= size(Seq)

ocl_ordset_subOrderedSet(OrdSet, Lower, Upper, Result) :-
   ocl_seq_subSequence(OrdSet, Lower, Upper, Result).

% ocl_ordset_at( +OrdSet, +Idx, -Result ) :- 
%    Return the element with position IDX within the set OrdSet
%    According to the precondition, 1 <= Idx <= size(Seq)

ocl_ordset_at(OrdSet, Idx, Result) :-
   ocl_seq_at(OrdSet, Idx, Result).
       
% ocl_ordset_first( +OrdSet, -Result ) :- 
%    Return the first element of the ordered set

ocl_ordset_first(OrdSet, Result) :-       
   ocl_seq_first(OrdSet, Result).
       
% ocl_ordset_last( +OrdSet, +Result ) :- 
%    Return the last element of the ordered set
ocl_ordset_last(OrdSet, Result) :-
   ocl_seq_last(OrdSet, Result).
       
       
       

              

%
% ECLiPSe libraries
%
:- lib(ic).     % Interval constraints
:- lib(apply).  % Using variables as functors

%------------------------------------------------------------------------------
%
% Logical operators - not, and, or, xor, implies, boolean equality, boolean
% disequality
% 
%------------------------------------------------------------------------------

%ocl_not(Instances, Vars, Predicate, Result) :-
%   Result is the logical "not" of the result of
%   a predicate

ocl_not(Instances, Vars, Predicate, Result) :-
   Result::0..1,
   apply(Predicate, [Instances, Vars, TruthValue]),
   ic:neg(TruthValue, Result).

%ocl_and(Instances, Vars, Pred1, Pred2, Result) :-
%   Result is the logical "and" among the results of the
%   two predicates

ocl_and(Instances, Vars, Pred1, Pred2, Result) :-
   Result::0..1,
   apply(Pred1, [Instances, Vars, TruthValue1]),
   apply(Pred2, [Instances, Vars, TruthValue2]),
   ic:and(TruthValue1, TruthValue2, Result).

%ocl_or(Instances, Vars, Pred1, Pred2, Result) :-
%   Result is the logical "or" among the results of the
%   two predicates

ocl_or(Instances, Vars, Pred1, Pred2, Result) :-
   Result::0..1,
   apply(Pred1, [Instances, Vars, TruthValue1]),
   apply(Pred2, [Instances, Vars, TruthValue2]),
   ic:or(TruthValue1, TruthValue2, Result).

%ocl_xor(Instances, Vars, Pred1, Pred2, Result) :-
%   Result is the exclusive "or" among the results of the
%   two predicates

ocl_xor(Instances, Vars, Pred1, Pred2, Result) :-
   Result::0..1,
   apply(Pred1, [Instances, Vars, TruthValue1]),
   apply(Pred2, [Instances, Vars, TruthValue2]),
   xor3(TruthValue1, TruthValue2, Result).

xor3(X, Y, Z) :- ic:neg(X, X1), ic:neg(Y, Y1), ic:and(X, Y1, Z1),
                 ic:and(X1, Y, Z2), ic:or(Z1, Z2, Z).

%ocl_implies(Instances, Vars, Pred1, Pred2, Result) :-
%   Result is true if Pred1 implies Pred2, and it is
%   false otherwise

ocl_implies(Instances, Vars, Pred1, Pred2, Result) :-
   Result::0..1,
   apply(Pred1, [Instances, Vars, TruthValue1]),
   apply(Pred2, [Instances, Vars, TruthValue2]),
   =>(TruthValue1, TruthValue2, Result).

%ocl_boolean_equals(Instances, Vars, Pred1, Pred2, Result) :-
%   Result is true if Pred1 is equal to Pred2, and it is
%   false otherwise

ocl_boolean_equals(Instances, Vars, Pred1, Pred2, Result) :-
   Result::0..1,
   apply(Pred1, [Instances, Vars, TruthValue1]),
   apply(Pred2, [Instances, Vars, TruthValue2]),
   #=(TruthValue1, TruthValue2, Result).

%ocl_boolean_not_equals(Instances, Vars, Pred1, Pred2, Result) :-
%   Result is true if Pred1 is not equal to Pred2, and it is
%   false otherwise

ocl_boolean_not_equals(Instances, Vars, Pred1, Pred2, Result) :-
   Result::0..1,
   apply(Pred1, [Instances, Vars, TruthValue1]),
   apply(Pred2, [Instances, Vars, TruthValue2]),
   #\=(TruthValue1, TruthValue2, Result).

%------------------------------------------------------------------------------
%
% Integer arithmetic and relational operators - minus, plus, times, div, 
% division, modulo, min, max, abs, <, >, <=, >=, ==, <>
% 
%------------------------------------------------------------------------------

%ocl_int_unary_minus(Instances, Vars, Predicate, Result) :-
%   Let X be the integer result of Predicate 
%   Result is -X

ocl_int_unary_minus(Instances, Vars, Predicate, Result) :-
   apply(Predicate, [Instances, Vars, X]),
   Result #= -X.

%ocl_int_binary_minus(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the integer result of Pred1
%   Let Y be the integer result of Pred2 
%   Result is X-Y

ocl_int_binary_minus(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result #= X-Y.

%ocl_int_plus(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the integer result of Pred1
%   Let Y be the integer result of Pred2 
%   Result is X-Y

ocl_int_plus(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result #= X+Y.

%ocl_int_times(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the integer result of Pred1
%   Let Y be the integer result of Pred2 
%   Result is X*Y

ocl_int_times(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result #= X*Y.

%ocl_int_division(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the integer result of Pred1
%   Let Y be the integer result of Pred2 
%   Result is X / Y, the real division of X and Y
ocl_int_division(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result $= X / Y.

%ocl_int_div(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the integer result of Pred1
%   Let Y be the integer result of Pred2 
%   Result is X div Y, the integer division of X and Y

ocl_int_div(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result #= X div Y.

%ocl_int_mod(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the integer result of Pred1
%   Let Y be the integer result of Pred2 
%   Result is X mod Y. This implementation uses the definition
%   of modulo provided in the OCL standard instead of the
%   built-in mod operator. 
%   X mod Y = (X - (X div Y)*Y)

ocl_int_mod(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result #= X - (X/Y)*Y.

%ocl_int_min(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the integer result of Pred1
%   Let Y be the integer result of Pred2 
%   Result is min(X,Y), the minimum of both results

ocl_int_min(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result #= min([X,Y]).

%ocl_int_max(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the integer result of Pred1
%   Let Y be the integer result of Pred2 
%   Result is max(X,Y), the maximum of both results

ocl_int_max(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result #= max([X,Y]).

%ocl_int_abs(Instances, Vars, Predicate, Result) :-
%   Let X be the integer result of Predicate 
%   Result is |X|, the absolute value of X

ocl_int_abs(Instances, Vars, Predicate, Result) :-
   apply(Predicate, [Instances, Vars, X]),
   Result #= abs(X).

%ocl_int_equals(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the integer result of Pred1
%   Let Y be the integer result of Pred2 
%   Result is true iff X = Y

ocl_int_equals(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result::0..1,
   #=(X, Y, Result).

%ocl_int_not_equals(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the integer result of Pred1
%   Let Y be the integer result of Pred2 
%   Result is true iff X <> Y

ocl_int_not_equals(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result::0..1,
   #\=(X, Y, Result).

%ocl_int_greater_than(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the integer result of Pred1
%   Let Y be the integer result of Pred2 
%   Result is true iff X > Y

ocl_int_greater_than(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result::0..1,
   #>(X, Y, Result).

%ocl_int_less_than(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the integer result of Pred1
%   Let Y be the integer result of Pred2 
%   Result is true iff X > Y

ocl_int_less_than(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result::0..1,
   #<(X, Y, Result).

%ocl_int_greater_equal(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the integer result of Pred1
%   Let Y be the integer result of Pred2 
%   Result is true iff X >= Y

ocl_int_greater_equal(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result::0..1,
   #>=(X, Y, Result).

%ocl_int_less_equal(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the integer result of Pred1
%   Let Y be the integer result of Pred2 
%   Result is true iff X > Y

ocl_int_less_equal(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result::0..1,
   #=<(X, Y, Result).

%------------------------------------------------------------------------------
%
% Real arithmetic and relational operators - minus, plus, times, division, min, 
% max, abs, floor, round, <, >, >=, <=, ==, <>
% 
%------------------------------------------------------------------------------

%ocl_real_unary_minus(Instances, Vars, Predicate, Result) :-
%   Let X be the real result of Predicate 
%   Result is -X

ocl_real_unary_minus(Instances, Vars, Predicate, Result) :-
   apply(Predicate, [Instances, Vars, X]),
   Result $= -X.

%ocl_real_binary_minus(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the real result of Pred1
%   Let Y be the real result of Pred2 
%   Result is X-Y

ocl_real_binary_minus(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result $= X-Y.

%ocl_real_plus(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the real result of Pred1
%   Let Y be the real result of Pred2 
%   Result is X-Y

ocl_real_plus(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result $= X+Y.

%ocl_real_times(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the real result of Pred1
%   Let Y be the real result of Pred2 
%   Result is X*Y

ocl_real_times(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result $= X*Y.

%ocl_real_division(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the real result of Pred1
%   Let Y be the real result of Pred2 
%   Result is X / Y, the real division of X and Y
ocl_real_division(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result $= X / Y.

%ocl_real_min(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the real result of Pred1
%   Let Y be the real result of Pred2 
%   Result is min(X,Y), the minimum of both results

ocl_real_min(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result $= min([X,Y]).

%ocl_real_max(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the real result of Pred1
%   Let Y be the real result of Pred2 
%   Result is max(X,Y), the maximum of both results

ocl_real_max(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result $= max([X,Y]).

%ocl_real_abs(Instances, Vars, Predicate, Result) :-
%   Let X be the real result of Predicate 
%   Result is |X|, the absolute value of X

ocl_real_abs(Instances, Vars, Predicate, Result) :-
   apply(Predicate, [Instances, Vars, X]),
   Result $= abs(X).

%ocl_real_floor(Instances, Vars, Predicate, Result) :-
%   Let X be the real result of Predicate 
%   Result is floor(X), rounding X down

ocl_real_floor(Instances, Vars, Predicate, Result) :-
   apply(Predicate, [Instances, Vars, X]),
   Result $= floor(X).

%ocl_real_round(Instances, Vars, Predicate, Result) :-
%   Let X be the real result of Predicate 
%   Result is floor(X), rounding X to the closest 
%   integer

ocl_real_round(Instances, Vars, Predicate, Result) :-
   apply(Predicate, [Instances, Vars, X]),
   Result $= round(X).

%ocl_real_equals(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the real result of Pred1
%   Let Y be the real result of Pred2 
%   Result is true iff X = Y

ocl_real_equals(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result::0..1,
   $=(X, Y, Result).

%ocl_real_not_equals(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the real result of Pred1
%   Let Y be the real result of Pred2 
%   Result is true iff X <> Y

ocl_real_not_equals(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result::0..1,
   $\=(X, Y, Result).

%ocl_real_greater_than(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the real result of Pred1
%   Let Y be the real result of Pred2 
%   Result is true iff X > Y

ocl_real_greater_than(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result::0..1,
   $>(X, Y, Result).

%ocl_real_less_than(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the real result of Pred1
%   Let Y be the real result of Pred2 
%   Result is true iff X > Y

ocl_real_less_than(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result::0..1,
   $<(X, Y, Result).

%ocl_real_greater_equal(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the real result of Pred1
%   Let Y be the real result of Pred2 
%   Result is true iff X >= Y

ocl_real_greater_equal(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result::0..1,
   $>=(X, Y, Result).

%ocl_real_less_equal(Instances, Vars, Pred1, Pred2, Result) :-
%   Let X be the real result of Pred1
%   Let Y be the real result of Pred2 
%   Result is true iff X > Y

ocl_real_less_equal(Instances, Vars, Pred1, Pred2, Result) :-
   apply(Pred1, [Instances, Vars, X]),
   apply(Pred2, [Instances, Vars, Y]),
   Result::0..1,
   $=<(X, Y, Result).

%------------------------------------------------------------------------------
%
% Base OCL operators - allInstances, VariableExp, navigation...
% 
%------------------------------------------------------------------------------

%ocl_allInstances(Instances, TypeName, Result) :-
%   Result is the set of instances of TypeName

ocl_allInstances(Instances, TypeName, Result) :-
   index(TypeName, Index),
   nth1(Index, Instances, Result).

%ocl_variable(Vars, NestingLevel, Result) :-
%   Result is the variable from Vars in position NestingLevel
%   Variable 1 is the variable defined in the innermost iterator, 
%   Var. 2 is defined in the next innermost iterator, ...

ocl_variable(Vars, NestingLevel, Result) :-
   nth1(NestingLevel, Vars, Result).

%ocl_attributeCall(Instances, TypeName, AttribName, Object, Result)  :-
%   Object is an instance of TypeName
%   TODO: inheritance (single and multiple), name hiding, ...

delay ocl_attributeCall(_, _, _, X, _) if var(X).
ocl_attributeCall(_, TypeName, AttribName, Object, Result)  :-
    attIndex(TypeName, AttribName, Index), 
    arg(Index, Object, Result).

% ocl_navigation(Instances, Vars, Association, SrcRole, DstRole, Objects, Result) :-
%    Navigation expression of an Association like Object.DstRole
%    - Association is the name of the association being navigated
%    - Objects is the value of the source object (or objects)
%    - SrcRole is the role where the source objects participate in Association,
%      the initial role of the navigation
%    - DstRole is the role of Association that we want to reach
%    - On output, Result becomes the set of objects that participate in DstRole 
%      such that some object from Objects participates in srcRole. If there is
%      only one object, instead of a list it become the first object of the set

delay ocl_navigation(_,_,_,_,X,_) if var(X).
ocl_navigation(Instances, Association, SrcRole, DstRole, Objects, Result) :-

   % Get the list of oids of the source objects
   ( is_list(Objects) -> 
    
     % Objects is a list of several objects
     getOidList(Objects, OidList) ;
 
     % Objects is a single object outside a list
     getOid(Objects,Oid),
     OidList = [Oid] 
   ),
 
   % Get the list of links of the association
   index(Association, AssocIndex),
   nth1(AssocIndex, Instances, LinkList),

   % Get the role indices
   roleIndex(Association, SrcRole, SrcIndex),
   roleIndex(Association, DstRole, DstIndex),

   % Get the set of links of the association where SrcIndex equals
   % an object within OidList. Returns a list of oids in the 
   % target relation
   aux_navigate(LinkList, SrcIndex, DstIndex, OidList, TargetOidList),
      
   % Get the set of objects of the target class   
   roleType(Association, DstRole, Type),
   index(Type, ClassIndex),
   nth1(ClassIndex, Instances, ObjectsOfType),

   % Select only those objects with an oid in the oid list
   aux_selectByOid(ObjectsOfType, TargetOidList, Result).

% aux_navigate(LinkList, SrcIndex, DstIndex, OidList, Result) :-
%    - LinkList is a list of links of an association
%    - SrcIndex is the input role for the navigation
%    - DstIndex is the output role for the association
%    - OidList is the list of valid oids in the input role
%    - Result should be assigned the list of valid oids in the
%      output role where a link with an oid from OidList in SrcRole
%      which have a corresponding Oid in OidList

delay aux_navigate(X,_,_,_,_) if nonground(X).
delay aux_navigate(_,_,_,Y,_) if nonground(Y).
aux_navigate(LinkList, SrcIndex, DstIndex, OidList, Result) :-
   ( foreach(Link, LinkList),
     fromto([], In, Out, Result),
     param(SrcIndex, DstIndex, OidList)
     do 
        arg(SrcIndex, Link, SrcValue),
        ( member(SrcValue, OidList) -> 
          % The target of this link should be added to the result
          arg(DstIndex, Link, DstValue),
          Out = [DstValue|In] ;
          % The target of this link should not be added to the result
          Out = In
        )
   ).

% aux_selectByOid(Instances, OidList, Result) :-
%    Result stores a list of objects from Instances with the given oids in OidList
%    If there is only one object, the result should be an object instead of a list

delay aux_selectByOid(X,_,_) if getOidList(X,Y), nonground(Y). 
delay aux_selectByOid(_,Z,_) if nonground(Z).
aux_selectByOid(Instances, OidList, Result) :-
   ( foreach(Object, Instances),
     fromto([], In, Out, ObjectList),
     param(OidList)
     do
        getOid(Object, Oid),
        ( member(Oid, OidList) ->
          % This object belongs to the solution
          Out = [Object|In];
          % This object does not belong to the solution
          Out = In )  
   ),
   % Check if the length of the list is one, in that case return the object
   % outside of the list
   ( length(ObjectList,1) ->
     ObjectList = [ Result ]; 
     Result = ObjectList
   ).
     
     

