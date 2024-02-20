Here is a small project based on the Wikidata API:

1- Query and download the end point result https://www.wikidata.org/wiki/Special:EntityData/Q42.json, 
This should be in JSON format, The id Q?? should be passed as argument to your script.
2- Extract entities.Q??.labels and entities.Q??.claims.P?? .
3- Sort Claims with mainsnak.datavalue.
4- Provide a search funcationlity which X matched value, search will look into datavalue.value 
and datavalue.datatype. Search partial text match .
5- if datavalue.value is number, print the min and max for that property value. 
if groupby option is provided, groupby will work on P???.datatype .
6- if two QID provide for the script, download both JSON from Wiki API and show Common pvalues, 
diff pvalues, common values for the same key. print these side by side
7- Provide a look functional cross multi QID similar to number 4. 
Please use what learnt from https://www.oreilly.com/library/view/python-cookbook-3rd/9781449357337/ch01.html#_unpacking_elements_from_iterables_of_arbitrary_length to solve the problem above



Python Cookbook - chapter 1

Collecitons module focus

What is a sequence?
https://www.pythontutorial.net/advanced-python/python-sequences/

