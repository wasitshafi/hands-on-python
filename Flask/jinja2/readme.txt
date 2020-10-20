All the html files should be in 'template' directory
css/java script files should be on 'static' directory

The jinja2 template engine uses the following delimiters for escaping from HTML

{% ... %} for Statements
{{ ... }} for Expressions to print to the template output
{# ... #} for Comments not included in the template output
# ... ## for Line Statements

Important attributes of request object are listed below :
1) Form    − It is a dictionary object containing key and value pairs of form parameters and their values.
2) args    − Parsed contents of query string which is part of URL after question mark (?).
3) Cookies − Dictionary object holding Cookie names and values.
4) files   − Data pertaining to uploaded file.
5) method  − Current request method.