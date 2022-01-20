:-lib(ic).
:-lib(apply).
:-lib(apply_macros).
:-lib(lists).

:- local struct(product(oid,stock)).
:- local struct(saleline(oid)).
:- local struct(sale(oid,paid,amount)).
:- local struct(portal(oid)).
:- local struct(goldcustomer(oid)).
:- local struct(customer(oid)).

:- local struct(salelineproduct(saleLine,product)).
:- local struct(includedin(sale,saleLine)).
:- local struct(purchases(customer,sale)).
:- local struct(registeredin(customer,portal)).

findSolutions(Snapshot,Parameters):-

	%Cardinality definitions
	SProduct::0..5, SSaleLine::0..5, SSale::0..5, SPortal::0..5, SGoldCustomer::0..5, SCustomer::0..5, 
	SsaleLineproduct::0..10, SIncludedIn::0..10, SPurchases::0..10, SRegisteredIn::0..10, 
	CardVariables=[SProduct, SSaleLine, SSale, SPortal, SGoldCustomer, SCustomer, SsaleLineproduct, SIncludedIn, SPurchases, SRegisteredIn],

	%Cardinality constraints
	strongSatisfiability(CardVariables),
	constraintsGenCustomerGoldCustomer(SCustomer, SGoldCustomer),

	constraintssaleLineproductCard(CardVariables),
	constraintsIncludedInCard(CardVariables),
	constraintsPurchasesCard(CardVariables),
	constraintsRegisteredInCard(CardVariables),

	%Instantiation of cardinality variables
	labeling(CardVariables),

	%Object creation
	creationProduct(OProduct, SProduct, AtProduct),
	creationSaleLine(OSaleLine, SSaleLine, AtSaleLine),
	creationSale(OSale, SSale, AtSale),
	creationPortal(OPortal, SPortal, AtPortal),
	creationGoldCustomer(OGoldCustomer, SGoldCustomer, AtGoldCustomer),
	creationCustomer(OCustomer, SCustomer, AtCustomer),

	differentOidsProduct(OProduct),
	differentOidsSaleLine(OSaleLine),
	differentOidsSale(OSale),
	differentOidsPortal(OPortal),
	differentOidsGoldCustomer(OGoldCustomer),
	differentOidsCustomer(OCustomer),

	orderedInstancesProduct(OProduct),
	orderedInstancesSaleLine(OSaleLine),
	orderedInstancesSale(OSale),
	orderedInstancesPortal(OPortal),
	orderedInstancesGoldCustomer(OGoldCustomer),
	orderedInstancesCustomer(OCustomer),

	existingOidsGoldCustomerInCustomer(OGoldCustomer, OCustomer),

	%Links creation
	creationsaleLineproduct(LsaleLineproduct, SsaleLineproduct, PsaleLineproduct, SSaleLine, SProduct),
	creationIncludedIn(LIncludedIn, SIncludedIn, PIncludedIn, SSale, SSaleLine),
	creationPurchases(LPurchases, SPurchases, PPurchases, SCustomer, SSale),
	creationRegisteredIn(LRegisteredIn, SRegisteredIn, PRegisteredIn, SCustomer, SPortal),

	differentLinkssaleLineproduct(LsaleLineproduct),
	differentLinksIncludedIn(LIncludedIn),
	differentLinksPurchases(LPurchases),
	differentLinksRegisteredIn(LRegisteredIn),

	orderedLinkssaleLineproduct(LsaleLineproduct),
	orderedLinksIncludedIn(LIncludedIn),
	orderedLinksPurchases(LPurchases),
	orderedLinksRegisteredIn(LRegisteredIn),

	Snapshot = [OProduct, OSaleLine, OSale, OPortal, OGoldCustomer, OCustomer, LsaleLineproduct, LIncludedIn, LPurchases, LRegisteredIn],

	cardinalityLinkssaleLineproduct(Snapshot),
	cardinalityLinksIncludedIn(Snapshot),
	cardinalityLinksPurchases(Snapshot),
	cardinalityLinksRegisteredIn(Snapshot),

	salesAmount(Snapshot),
	minStock(Snapshot),

	preAddSaleLine(Snapshot, Parameters, Result),

	AllAttributes = [PsaleLineproduct, PIncludedIn, PPurchases, PRegisteredIn, AtProduct, AtSaleLine, AtSale, AtPortal, AtGoldCustomer, AtCustomer],
	append(AllAttributes,Parameters,AllAttributes),
	flatten(AllAttributes, Attributes),

	%Instantiation of attributes values
	labeling(Attributes).

constraintsGenCustomerGoldCustomer(SCustomer, SGoldCustomer):-
	constraintsSubtypesCard(SCustomer, [SGoldCustomer]).

index("Product", 1).
index("SaleLine", 2).
index("Sale", 3).
index("Portal", 4).
index("GoldCustomer", 5).
index("Customer", 6).
index("saleLineproduct", 7).
index("IncludedIn", 8).
index("Purchases", 9).
index("RegisteredIn", 10).

attIndex("Product", "stock", 2).
attIndex("Sale", "paid", 2).
attIndex("Sale", "amount", 3).

roleIndex("saleLineproduct", "saleLine", 1).
roleIndex("saleLineproduct", "product", 2).
roleIndex("IncludedIn", "sale", 1).
roleIndex("IncludedIn", "saleLine", 2).
roleIndex("Purchases", "customer", 1).
roleIndex("Purchases", "sale", 2).
roleIndex("RegisteredIn", "customer", 1).
roleIndex("RegisteredIn", "portal", 2).

roleType("saleLineproduct", "saleLine", "SaleLine").
roleType("saleLineproduct", "product", "Product").
roleType("IncludedIn", "sale", "Sale").
roleType("IncludedIn", "saleLine", "SaleLine").
roleType("Purchases", "customer", "Customer").
roleType("Purchases", "sale", "Sale").
roleType("RegisteredIn", "customer", "Customer").
roleType("RegisteredIn", "portal", "Portal").

roleMin("saleLineproduct", "saleLine", 0).
roleMin("saleLineproduct", "product", 1).
roleMin("IncludedIn", "sale", 1).
roleMin("IncludedIn", "saleLine", 1).
roleMin("Purchases", "customer", 1).
roleMin("Purchases", "sale", 0).
roleMin("RegisteredIn", "customer", 0).
roleMin("RegisteredIn", "portal", 1).

roleMax("saleLineproduct", "saleLine", "*").
roleMax("saleLineproduct", "product", 1).
roleMax("IncludedIn", "sale", 1).
roleMax("IncludedIn", "saleLine", "*").
roleMax("Purchases", "customer", 1).
roleMax("Purchases", "sale", "*").
roleMax("RegisteredIn", "customer", "*").
roleMax("RegisteredIn", "portal", 1).

assocIsUnique("saleLineproduct", 1).
assocIsUnique("IncludedIn", 1).
assocIsUnique("Purchases", 1).
assocIsUnique("RegisteredIn", 1).

isSubTypeOf("GoldCustomer", "Customer").

strongSatisfiability(CardVariables):- strongSatisfiabilityConstraint(CardVariables).


constraintssaleLineproductCard(CardVariables):-constraintsBinAssocMultiplicities("saleLineproduct", "saleLine", "product", CardVariables).
constraintsIncludedInCard(CardVariables):-constraintsBinAssocMultiplicities("IncludedIn", "sale", "saleLine", CardVariables).
constraintsPurchasesCard(CardVariables):-constraintsBinAssocMultiplicities("Purchases", "customer", "sale", CardVariables).
constraintsRegisteredInCard(CardVariables):-constraintsBinAssocMultiplicities("RegisteredIn", "customer", "portal", CardVariables).

creationProduct(Instances, Size, Attributes):-
	length(Instances, Size),
	(foreach(Xi, Instances), fromto([],AtIn,AtOut,Attributes), param(Size) do
		Xi=product{oid:Integer1,stock:Integer2}, Integer1::1..Size, Integer2::0..10, 
		append([Integer1,Integer2],AtIn, AtOut)).

creationSaleLine(Instances, Size, Attributes):-
	length(Instances, Size),
	(foreach(Xi, Instances), fromto([],AtIn,AtOut,Attributes), param(Size) do
		Xi=saleline{oid:Integer1}, Integer1::1..Size, 
		append([Integer1],AtIn, AtOut)).

creationSale(Instances, Size, Attributes):-
	length(Instances, Size),
	(foreach(Xi, Instances), fromto([],AtIn,AtOut,Attributes), param(Size) do
		Xi=sale{oid:Integer1,paid:Boolean2,amount:Integer3}, Integer1::1..Size, Boolean2::0..1, Integer3::0..10, 
		append([Integer1,Boolean2,Integer3],AtIn, AtOut)).

creationPortal(Instances, Size, Attributes):-
	length(Instances, Size),
	(foreach(Xi, Instances), fromto([],AtIn,AtOut,Attributes), param(Size) do
		Xi=portal{oid:Integer1}, Integer1::1..Size, 
		append([Integer1],AtIn, AtOut)).

creationGoldCustomer(Instances, Size, Attributes):-
	length(Instances, Size),
	(foreach(Xi, Instances), fromto([],AtIn,AtOut,Attributes), param(Size) do
		Xi=goldcustomer{oid:Integer1}, Integer1::1..Size, 
		append([Integer1],AtIn, AtOut)).

creationCustomer(Instances, Size, Attributes):-
	length(Instances, Size),
	(foreach(Xi, Instances), fromto([],AtIn,AtOut,Attributes), param(Size) do
		Xi=customer{oid:Integer1}, Integer1::1..Size, 
		append([Integer1],AtIn, AtOut)).

differentOidsProduct(Instances) :- differentOids(Instances).
differentOidsSaleLine(Instances) :- differentOids(Instances).
differentOidsSale(Instances) :- differentOids(Instances).
differentOidsPortal(Instances) :- differentOids(Instances).
differentOidsGoldCustomer(Instances) :- differentOids(Instances).
differentOidsCustomer(Instances) :- differentOids(Instances).

orderedInstancesProduct(Instances) :- orderedInstances(Instances).
orderedInstancesSaleLine(Instances) :- orderedInstances(Instances).
orderedInstancesSale(Instances) :- orderedInstances(Instances).
orderedInstancesPortal(Instances) :- orderedInstances(Instances).
orderedInstancesGoldCustomer(Instances) :- orderedInstances(Instances).
orderedInstancesCustomer(Instances) :- orderedInstances(Instances).

existingOidsGoldCustomerInCustomer(OGoldCustomer, OCustomer):-existsOidIn(OGoldCustomer, OCustomer).

creationsaleLineproduct(Instances, Size, Participants, SSaleLine, SProduct):-
	length(Instances, Size),
	(foreach(Xi, Instances), fromto([],AtIn,AtOut,Participants), param(SSaleLine), param(SProduct) do
		Xi=salelineproduct{saleLine:ValuePart1,product:ValuePart2}, ValuePart1#>0, ValuePart1#=<SSaleLine, ValuePart2#>0, ValuePart2#=<SProduct,
		append([ValuePart1, ValuePart2],AtIn, AtOut)).

creationIncludedIn(Instances, Size, Participants, SSale, SSaleLine):-
	length(Instances, Size),
	(foreach(Xi, Instances), fromto([],AtIn,AtOut,Participants), param(SSale), param(SSaleLine) do
		Xi=includedin{sale:ValuePart1,saleLine:ValuePart2}, ValuePart1#>0, ValuePart1#=<SSale, ValuePart2#>0, ValuePart2#=<SSaleLine,
		append([ValuePart1, ValuePart2],AtIn, AtOut)).

creationPurchases(Instances, Size, Participants, SCustomer, SSale):-
	length(Instances, Size),
	(foreach(Xi, Instances), fromto([],AtIn,AtOut,Participants), param(SCustomer), param(SSale) do
		Xi=purchases{customer:ValuePart1,sale:ValuePart2}, ValuePart1#>0, ValuePart1#=<SCustomer, ValuePart2#>0, ValuePart2#=<SSale,
		append([ValuePart1, ValuePart2],AtIn, AtOut)).

creationRegisteredIn(Instances, Size, Participants, SCustomer, SPortal):-
	length(Instances, Size),
	(foreach(Xi, Instances), fromto([],AtIn,AtOut,Participants), param(SCustomer), param(SPortal) do
		Xi=registeredin{customer:ValuePart1,portal:ValuePart2}, ValuePart1#>0, ValuePart1#=<SCustomer, ValuePart2#>0, ValuePart2#=<SPortal,
		append([ValuePart1, ValuePart2],AtIn, AtOut)).

differentLinkssaleLineproduct(X):- differentLinks(X).
differentLinksIncludedIn(X):- differentLinks(X).
differentLinksPurchases(X):- differentLinks(X).
differentLinksRegisteredIn(X):- differentLinks(X).

orderedLinkssaleLineproduct(X):- orderedLinks(X).
orderedLinksIncludedIn(X):- orderedLinks(X).
orderedLinksPurchases(X):- orderedLinks(X).
orderedLinksRegisteredIn(X):- orderedLinks(X).

cardinalityLinkssaleLineproduct(Instances):-
	linksConstraintMultiplicities(Instances, "saleLineproduct","saleLine","product").
cardinalityLinksIncludedIn(Instances):-
	linksConstraintMultiplicities(Instances, "IncludedIn","sale","saleLine").
cardinalityLinksPurchases(Instances):-
	linksConstraintMultiplicities(Instances, "Purchases","customer","sale").
cardinalityLinksRegisteredIn(Instances):-
	linksConstraintMultiplicities(Instances, "RegisteredIn","customer","portal").

nallInstances1salesAmount( Instances, _, Result):-
	ocl_allInstances(Instances, "GoldCustomer", Result).

nVariable2_1_1_1_1_1salesAmount( _, Vars, Result):-
	ocl_variable(Vars,1,Result).

nNavigation2_1_1_1_1salesAmount( Instances, Vars, Result):-
	nVariable2_1_1_1_1_1salesAmount(Instances, Vars, Value1),
	ocl_navigation(Instances, "Purchases", "customer", "sale", Value1, Result).

nVariable2_1_1_1_2_1salesAmount( _, Vars, Result):-
	ocl_variable(Vars,1,Result).

nAttribute2_1_1_1_2salesAmount( Instances, Vars, Result):-
	nVariable2_1_1_1_2_1salesAmount(Instances, Vars, Object),
	ocl_attributeCall(Instances, "Sale", "paid", Object, Result).

nselect2_1_1_1salesAmount( Instances, Vars, Result):-
	nNavigation2_1_1_1_1salesAmount(Instances, Vars, Value1),
	ocl_set_select(Instances, Vars, Value1, nAttribute2_1_1_1_2salesAmount, Result).

nVariable2_1_1_2_1salesAmount( _, Vars, Result):-
	ocl_variable(Vars,1,Result).

nAttribute2_1_1_2salesAmount( Instances, Vars, Result):-
	nVariable2_1_1_2_1salesAmount(Instances, Vars, Object),
	ocl_attributeCall(Instances, "Sale", "amount", Object, Result).

ncollect2_1_1salesAmount( Instances, Vars, Result):-
	nselect2_1_1_1salesAmount(Instances, Vars, Value1),
	ocl_bag_collect(Instances, Vars, Value1, nAttribute2_1_1_2salesAmount, Result).

nsum2_1salesAmount( Instances, Vars, Result):-
	ncollect2_1_1salesAmount(Instances, Vars, Value1),
	ocl_bag_sum(Value1, Result).

nConstant2_2salesAmount( _, _, Result):-
	Result=100000.

ngreater_than2salesAmount( Instances, Vars, Result):-
	ocl_int_greater_than(Instances, Vars, nsum2_1salesAmount, nConstant2_2salesAmount, Result).

nforAll0salesAmount( Instances, Vars, Result):-
	nallInstances1salesAmount(Instances, Vars, Value1),
	ocl_col_forAll(Instances, Vars, Value1, ngreater_than2salesAmount, Result).

salesAmount(Instances):-
	nforAll0salesAmount(Instances, [], Result),
	Result #=1.


nallInstances1minStock( Instances, _, Result):-
	ocl_allInstances(Instances, "Product", Result).

nVariable2_1_1minStock( _, Vars, Result):-
	ocl_variable(Vars,1,Result).

nAttribute2_1minStock( Instances, Vars, Result):-
	nVariable2_1_1minStock(Instances, Vars, Object),
	ocl_attributeCall(Instances, "Product", "stock", Object, Result).

nConstant2_2minStock( _, _, Result):-
	Result=5.

ngreater_equal2minStock( Instances, Vars, Result):-
	ocl_int_greater_equal(Instances, Vars, nAttribute2_1minStock, nConstant2_2minStock, Result).

nforAll0minStock( Instances, Vars, Result):-
	nallInstances1minStock(Instances, Vars, Value1),
	ocl_col_forAll(Instances, Vars, Value1, ngreater_equal2minStock, Result).

minStock(Instances):-
	nforAll0minStock(Instances, [], Result),
	Result #=1.


nVariable1_1addSaleLinepre( _, Vars, Result):-
	ocl_variable(Vars,2,Result).

nAttribute1addSaleLinepre( Instances, Vars, Result):-
	nVariable1_1addSaleLinepre(Instances, Vars, Object),
	ocl_attributeCall(Instances, "Product", "stock", Object, Result).

nConstant2addSaleLinepre( _, _, Result):-
	Result=0.

ngreater_than0addSaleLinepre( Instances, Vars, Result):-
	ocl_int_greater_than(Instances, Vars, nAttribute1addSaleLinepre, nConstant2addSaleLinepre, Result).

preAddSaleLine(Snapshot, Parameters, Result):-
	Parameters = [result,quantity,p,self],
	parameterOfObjectType(result, Snapshot, "SaleLine"),
	parameterOfBasicType(quantity, 0..10),
	parameterOfObjectType(p, Snapshot, "Product"),
	parameterOfObjectType(self, Snapshot, "Sale"),

	ngreater_than0addSaleLinepre(Snapshot, Parameters, Result),	Result #=1.


