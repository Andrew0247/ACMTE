# ACMTE
Project of an Application to Support the Construction of Theoretical Frames.

The following project is done in <Code> python </Code>. The file <Code> Interfaz_App2.py </Code> must be executed to carry out the respective processes which will help in the creation of a theoretical framework.

To use this project, the following libraries must be installed:
<ul>
  <li><a href="https://numpy.org/">Numpy</a>: <Code>pip install numpy</Code>.>/li>
  <li><a href="https://www.nltk.org/">NLTK</a>: <Code>pip install nltk</Code></li>
  <li><a href="https://spacy.io/">spaCy</a>: <Code>pip install spacy</Code>.</li>
  <li>Models of spaCy: <Code>python -m spacy download en_core_web_sm</Code>, it is recommended to install the large model, more information by clicking <a href="https://spacy.io/models">here</a>.</li>
  <li><a href="https://radimrehurek.com/gensim/">Gensim</a>: <Code>pip install gensim</Code>. Used to incorporate the LDA algorithm.</li>
  <li><a href="https://matplotlib.org/">Matplotlib</a>: Used to make graphs.</a>
  <li><a href="https://pandas.pydata.org/">Pandas</a>: Used to better process the text of the articles.</li>
  <li><a href="https://networkx.github.io/">Networkx</a>: Used to graph the graph of most concurrent synonyms in the text, which we remove with spaCy. Your installation command <Code>pip install networkx</Code>.</li>
  <li><a href="https://pythonhosted.org/easygui/index.html">Easygui</a>: Used to open directories with a popup window. Your installation command <Code>pip install easygui</Code>.</li>
  <li><a href="https://docs.python.org/3/library/tkinter.html">Tkinter</a>: Used to make graphical interfaces in an intuitive way, so to speak. It usually comes installed by default with python.</li>
</ul>
  
A library called **MyNLP** is also used, which is used to extract the different definitions of the **most frequent synonyms** in the text. A method for graphing **Graphs** is added, with which the **hyperonyms** of the synonyms of the text would be visualized. It should be noted that the **MyNLP** library is created by **Magister Hector Andrés Mora**, you can visit his repository by clicking <a href="https://github.com/magohector">here</a>.
