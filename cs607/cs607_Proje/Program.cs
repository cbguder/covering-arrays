using System;
using System.Collections.Generic;
using System.Text;
using System.Xml;
using System.IO;

namespace cs607_Proje
{
    class Option
    {
        private string name;
        private List<string> valueList;

        public Option()
        {
            name = "";
            valueList = new List<string>();
        }

        public Option(string optionName, List<string> optionValues)
        {
            name = optionName;
            valueList = new List<string>();

            for (int a = 0; a < optionValues.Count; a++)
            {
                string temp = optionValues[a];
                valueList.Add(temp);
            }
        }

        public Option(string optionName)
        {
            name = optionName;
            valueList = new List<string>();
        }

        public void pushValue(string param1)
        {
            valueList.Add(param1);
        }

        public List<string> getValueList()
        {
            List<string> result = new List<string>();
            for (int a = 0; a < valueList.Count; a++)
                result.Add(valueList[a]);
            return result;
        }

        public string getOptionName()
        {
            return name;
        }

        public int countValues()
        {
            return valueList.Count;
        }
    }

    class Item
    {
        private string objectName;
        private string objectValue;

        public Item()
        {
            objectName = "";
            objectValue = "";
        }

        public Item(string name, string value)
        {
            objectName = name;
            objectValue = value;
        }

        public string getObjectName()
        {
            return objectName;
        }

        public string getObjectValue()
        {
            return objectValue;
        }

        public void setObjectValue(string param1)
        {
            objectValue = param1;
        }

        public void setObjectName(string param1)
        {
            objectName = param1;
        }

        public void setEqualTo(Item param1)
        {
            setObjectName(param1.getObjectName());
            setObjectValue(param1.getObjectValue());
        }
    }

    class Rule
    {
        private string result;
        private List<Item> itemList;

        public Rule()
        {
            result = "";
            itemList = new List<Item>();
        }

        public Rule(string param1, List<Item> param2)
        {
            result = param1;

            itemList = new List<Item>();

            for (int a = 0; a < param2.Count; a++)
            {
                Item temp = new Item();
                temp.setEqualTo(param2[a]);
                itemList.Add(temp);
            }
        }

        public string getResult()
        {
            return result;
        }

        public void setResult(string param1)
        {
            result = param1;
        }

        public List<Item> getItemList()
        {
            List<Item> temp = new List<Item>();

            for (int a = 0; a < itemList.Count; a++)
            {
                Item tempItem = new Item();
                tempItem.setEqualTo(itemList[a]);
                temp.Add(tempItem);
            }

            return temp;
        }

        public void setItemList(List<Item> param1)
        {
            itemList.Clear();

            for (int a = 0; a < param1.Count; a++)
            {
                Item temp = new Item();
                temp.setEqualTo(param1[a]);
                itemList.Add(temp);
            }
        }

        public void setEqualTo(Rule rhs)
        {
            setResult(rhs.getResult());
            setItemList(rhs.getItemList());
        }
    }

    class Configuration
    {
        private string result;
        private List<Item> itemList;

        public Configuration()
        {
            result = "";
            itemList = new List<Item>();
        }

        public Configuration(string param1, List<Item> param2)
        {
            result = param1;

            itemList = new List<Item>();

            for (int a = 0; a < param2.Count; a++)
            {
                Item tempItem = new Item();
                tempItem.setEqualTo(param2[a]);
                itemList.Add(tempItem);
            }
        }

        public string getResult()
        {
            return result;
        }

        public void setResult(string param1)
        {
            result = param1;
        }

        public List<Item> getItemList()
        {
            List<Item> result = new List<Item>();

            for (int a = 0; a < itemList.Count; a++)
            {
                Item temp = new Item();
                temp.setEqualTo(itemList[a]);
                result.Add(temp);
            }
            return result;
        }

        public void setItemList(List<Item> param1)
        {
            itemList.Clear();

            for (int a = 0; a < param1.Count; a++)
            {
                Item temp = new Item();
                temp.setEqualTo(param1[a]);
                itemList.Add(temp);
            }
        }

        public void changeItemValue(string itemName, string newValue)
        {
            for (int a = 0; a < itemList.Count; a++)
            {
                if (itemList[a].getObjectName()== itemName)
                {
                    itemList[a].setObjectValue(newValue);
                    break;
                }
            }
        }

        public void setEqualTo(Configuration rhs)
        {
            setResult(rhs.getResult());
            setItemList(rhs.getItemList());
        }
    }

    class Triplet
    {
        private Configuration original;
        private Configuration changed;
        private int score;

        public Triplet()
        {
            original = new Configuration();
            changed = new Configuration();
            score = 0;
        }

        public Triplet(Configuration orig, Configuration chan, int sco)
        {
            original = new Configuration();
            original.setEqualTo(orig);

            changed = new Configuration();
            changed.setEqualTo(chan);

            score = sco;
        }

        public void setOriginalConf(Configuration param1)
        {
            original.setEqualTo(param1);
        }

        public void setChangedConf(Configuration param1)
        {
            changed.setEqualTo(param1);
        }

        public void setScore(int param1)
        {
            score = param1;
        }

        public int getScore()
        {
            return score;
        }

        public Configuration getOriginalConf()
        {
            Configuration result = new Configuration();
            result.setEqualTo(original);
            return result;
        }

        public Configuration getChangedConf()
        {
            Configuration result = new Configuration();
            result.setEqualTo(changed);
            return result;
        }

        public void setEqualTo(Triplet param1)
        {
            setChangedConf(param1.getChangedConf());
            setOriginalConf(param1.getOriginalConf());
            setScore(param1.getScore());
        }
    }

    class Testcase
    {
        private string id;
        private int score;
        private List<Configuration> PassingList = new List<Configuration>();
        private List<Configuration> FailingList = new List<Configuration>();
        private List<Configuration> AddedList = new List<Configuration>();
        private List<Rule> RuleList = new List<Rule>();
        private List<string> CoveringListOptions = new List<string>();

        public Testcase()
        {
            id = "";
            score = 0;
        }

        public void setId(string param1)
        {
            id = param1;
        }

        public string getId()
        {
            return id;
        }

        public void setScore(int param1)
        {
            score = param1;
        }

        public int getScore()
        {
            return score;
        }

        public void setPassingList(List<Configuration> param1)
        {
            PassingList.Clear();
            for (int a = 0; a < param1.Count; a++)
            {
                Configuration temp = new Configuration();
                temp.setEqualTo(param1[a]);

                PassingList.Add(temp);
            }
        }

        public List<Configuration> getPassingList()
        {
            List<Configuration> result = new List<Configuration>();

            for (int a = 0; a < PassingList.Count; a++)
            {
                Configuration temp = new Configuration();
                temp.setEqualTo(PassingList[a]);
                result.Add(temp);
            }
            return result;
        }

        public void setFailingList(List<Configuration> param1)
        {
            FailingList.Clear();
            for (int a = 0; a < param1.Count; a++)
            {
                Configuration temp = new Configuration();
                temp.setEqualTo(param1[a]);

                FailingList.Add(temp);
            }
        }

        public List<Configuration> getFailingList()
        {
            List<Configuration> result = new List<Configuration>();

            for (int a = 0; a < FailingList.Count; a++)
            {
                Configuration temp = new Configuration();
                temp.setEqualTo(FailingList[a]);
                result.Add(temp);
            }
            return result;
        }

        public void setAddedList(List<Configuration> param1)
        {
            AddedList.Clear();
            for (int a = 0; a < param1.Count; a++)
            {
                Configuration temp = new Configuration();
                temp.setEqualTo(param1[a]);

                AddedList.Add(temp);
            }
        }

        public List<Configuration> getAddedList()
        {
            List<Configuration> result = new List<Configuration>();

            for (int a = 0; a < AddedList.Count; a++)
            {
                Configuration temp = new Configuration();
                temp.setEqualTo(AddedList[a]);
                result.Add(temp);
            }
            return result;
        }

        public void addNewConfiguration(Configuration param1)
        {
            Configuration temp = new Configuration();
            temp.setEqualTo(param1);

            AddedList.Add(temp);
        }

        public void setRuleList(List<Rule> param1)
        {
            RuleList.Clear();
            for (int a = 0; a < param1.Count; a++)
            {
                Rule temp = new Rule();
                temp.setEqualTo(param1[a]);

                RuleList.Add(temp);
            }
        }

        public List<Rule> getRuleList()
        {
            List<Rule> result = new List<Rule>();
            for (int a = 0; a < RuleList.Count; a++)
            {
                Rule temp = new Rule();
                temp.setEqualTo(RuleList[a]);

                result.Add(temp);
            }
            return result;
        }

        public void addRule(Rule param1)
        {
            Rule temp = new Rule();
            temp.setEqualTo(param1);

            RuleList.Add(temp);
        }

        public void setCoveringListOptions(List<string> param1)
        {
            CoveringListOptions.Clear();

            for (int a = 0; a < param1.Count; a++)
            {
                string temp = param1[a];
                CoveringListOptions.Add(temp);
            }
        }

        public List<string> getCoveringListOptions()
        {
            List<string> result = new List<string>();

            for (int a = 0; a < CoveringListOptions.Count; a++)
            {
                string temp = CoveringListOptions[a];
                result.Add(temp);
            }
            return result;
        }

        public void printPassingList()
        {
            Console.WriteLine("-----PRINTING PASSING CONFIGURATION LIST-----");
            Console.WriteLine("-----Test ID = " + id + "--------------------");
            for (int a = 0; a < PassingList.Count; a++)
            {
                string result = PassingList[a].getResult();
                List<Item> tempList = PassingList[a].getItemList();

                Console.Write("result=" + result + " ");

                for (int b = 0; b < tempList.Count; b++)
                {
                    Item temp = new Item();
                    temp.setEqualTo(tempList[b]);

                    Console.Write(temp.getObjectName() + "=" + temp.getObjectValue() + " ");
                }
                Console.Write("\n");
            }
        }

        public void printFailingList()
        {
            Console.WriteLine("-----PRINTING FAILING CONFIGURATION LIST-----");
            Console.WriteLine("-----Test ID = " + id + "--------------------");
            for (int a = 0; a < FailingList.Count; a++)
            {
                string result = FailingList[a].getResult();
                List<Item> tempList = FailingList[a].getItemList();

                Console.Write("result=" + result + " ");

                for (int b = 0; b < tempList.Count; b++)
                {
                    Item temp = new Item();
                    temp.setEqualTo(tempList[b]);

                    Console.Write(temp.getObjectName() + "=" + temp.getObjectValue() + " ");
                }
                Console.Write("\n");
            }
        }

        public void printAddedList()
        {
            Console.WriteLine("-----PRINTING ADDED CONFIGURATION LIST-----");
            Console.WriteLine("-----Test ID = " + id + "--------------------");
            for (int a = 0; a < AddedList.Count; a++)
            {
                string result = AddedList[a].getResult();
                List<Item> tempList = AddedList[a].getItemList();

                Console.Write("result=" + result + " ");

                for (int b = 0; b < tempList.Count; b++)
                {
                    Item temp = new Item();
                    temp.setEqualTo(tempList[b]);

                    Console.Write(temp.getObjectName() + "=" + temp.getObjectValue() + " ");
                }
                Console.Write("\n");
            }
        }

        public void printRuleList()
        {
            Console.WriteLine("-----PRINTING RULE LIST-----");
            Console.WriteLine("-----Test ID = " + id + "--------------------");
            for (int a = 0; a < RuleList.Count; a++)
            {
                string result = RuleList[a].getResult();
                List<Item> tempList = RuleList[a].getItemList();

                Console.Write("result=" + result + " ");

                for (int b = 0; b < tempList.Count; b++)
                {
                    Item temp = new Item();
                    temp.setEqualTo(tempList[b]);

                    Console.Write(temp.getObjectName() + "=" + temp.getObjectValue() + " ");
                }

                Console.Write("\n");
            }
        }
    }


    class Program
    {
        static List<Testcase> TESTCASE_LIST = new List<Testcase>();
        static List<Option> OPTION_LIST = new List<Option>();
        static List<Triplet> TRIPLET_LIST = new List<Triplet>();
        static bool CHOOSE_GLOBAL = false;
        

        //Parses options file, which specificies the distint configuration objects, and the values it can take
        //Does not check if the filename exists, if it does not exist that the program will fail
        static void parseOptionsXML(string filename)
        {
            FileStream reader = new FileStream(filename, FileMode.Open, FileAccess.Read, FileShare.ReadWrite);
            XmlDocument compSpecs = new XmlDocument();
            compSpecs.Load(reader);

            XmlNodeList nodeList = compSpecs.GetElementsByTagName("option");

            OPTION_LIST.Clear();

            //for all the "option" nodes in the list
            for (int counter = 0; counter < nodeList.Count; counter++)
            {
                //get object name
                XmlAttribute nameAttr = nodeList[counter].Attributes[0];
                string name = nameAttr.Value;

                Option dummy = new Option(name);

                //get the values that option can take as a list
                XmlNodeList childList = nodeList[counter].ChildNodes;
                for (int a = 0; a < childList.Count; a++)
                {
                    string value = childList[a].InnerText;
                    dummy.pushValue(value);
                }

                OPTION_LIST.Add(dummy);
            }

            OPTION_LIST.Sort(delegate(Option a, Option b) { return a.getOptionName().CompareTo(b.getOptionName()); });
            reader.Close();
        }

        //Function to print out the elements of OPTION_LIST
        //This function is for debugging purpose only
        static void printOptionList()
        {
            Console.WriteLine("-----PRINTING OPTION LIST-----");
            for (int a = 0; a < OPTION_LIST.Count; a++)
            {
                string optionName = OPTION_LIST[a].getOptionName();
                List<string> valueList = OPTION_LIST[a].getValueList();

                Console.Write(optionName + ": ");

                for (int b = 0; b < valueList.Count; b++)
                {
                    Console.Write(valueList[b] + " ");
                }

                Console.Write("\n");
            }
        }

        //Parses configuration file, which contains information about configurations that have been tested and their results
        //Passing configuration's result is "p", otherwise that configuration is counted as failing configuration
        //It is assumed that a configuration consists of all options previously parsed
        static void parseConfigurationsXML(string filename)
        {
            FileStream reader = new FileStream(filename, FileMode.Open, FileAccess.Read, FileShare.ReadWrite);
            XmlDocument compSpecs = new XmlDocument();
            compSpecs.Load(reader);

            XmlNodeList nodeList = compSpecs.GetElementsByTagName("test");

            for (int counter = 0; counter < nodeList.Count; counter++)
            {
                Testcase testcaseToAdd = new Testcase();

                XmlNode currentTestNode = nodeList[counter];

                //set test id
                string testId = currentTestNode.Attributes[0].Value;
                testcaseToAdd.setId(testId);

                List<Configuration> passList = new List<Configuration>();
                List<Configuration> failList = new List<Configuration>();

                //get children nodes, which are configuration nodes
                XmlNodeList childNodes = nodeList[counter].ChildNodes;
                for (int a = 0; a < childNodes.Count; a++)
                {
                    XmlNode configNode = childNodes[a];

                    //get configuration result
                    string configResult = configNode.Attributes[0].Value;
                    
                    List<Item> optionList = new List<Item>();

                    //get children nodes, which are option nodes
                    XmlNodeList optionNodes = configNode.ChildNodes;
                    for (int b = 0; b < optionNodes.Count; b++)
                    {
                        string optionName = optionNodes[b].Attributes[0].Value;
                        string optionValue = optionNodes[b].InnerText;

                        Item dummy = new Item(optionName, optionValue);
                        optionList.Add(dummy);
                    }

                    optionList.Sort(delegate(Item aa, Item bb) { return aa.getObjectName().CompareTo(bb.getObjectName()); });

                    Configuration toAdd = new Configuration(configResult, optionList);

                    if (configResult == "p")
                        passList.Add(toAdd);
                    else
                        failList.Add(toAdd);
                }

                testcaseToAdd.setPassingList(passList);
                testcaseToAdd.setFailingList(failList);

                TESTCASE_LIST.Add(testcaseToAdd);
            }

            reader.Close();
        }
                      
        //Parses decision tree file, which contains information about rules of configurations
        //recursively calls parseDTXML function
        static void parseDecisionTreeXML(string filename)
        {
            FileStream reader = new FileStream(filename, FileMode.Open, FileAccess.Read, FileShare.ReadWrite);
            XmlDocument compSpecs = new XmlDocument();
            compSpecs.Load(reader);

            XmlNodeList nodeList = compSpecs.GetElementsByTagName("tree");

            //for every tree node
            for (int counter = 0; counter < nodeList.Count; counter++)
            {
                XmlNode testNode = nodeList[counter];

                //get test id
                string testId = testNode.Attributes[1].Value;

                //find the location of the test with that id
                int location = -1;
                for (int a = 0; a < TESTCASE_LIST.Count; a++)
                {
                    if (testId == TESTCASE_LIST[a].getId())
                        location = a;
                }

                //if we find the testcase with that testId 
                if (location != -1)
                {
                    XmlNodeList ruleNodes = testNode.ChildNodes;
                    for (int x = 0; x < ruleNodes.Count; x++)
                    {
                        List<Item> list = new List<Item>();
                        parseDTXML(ruleNodes[x], list, location);
                    }

                    //calculate covering options list
                    //get the rule list
                    List<Rule> ruleList = TESTCASE_LIST[location].getRuleList();
                    List<string> coveringList = new List<string>();
                    //for every rule in the list
                    for (int x = 0; x < ruleList.Count; x++)
                    {
                        Rule tempRule = new Rule();
                        tempRule.setEqualTo(ruleList[x]);

                        //get the item list for that rule
                        List<Item> itemList = tempRule.getItemList();

                        //for every item in the rule
                        for (int y = 0; y < itemList.Count; y++)
                        {
                            string optionName = itemList[y].getObjectName();
                            //if that option is not added to the list so far add it to the covering option list
                            addToList(coveringList, optionName);
                        }
                    }
                    TESTCASE_LIST[location].setCoveringListOptions(coveringList);
                }
            }

            reader.Close();
        }

        static void addToList(List<string> param1, string param2)
        {
            for (int a = 0; a < param1.Count; a++)
            {
                if (param1[a] == param2)
                    return;
            }
            param1.Add(param2);
        }

        //if the node is a "test" node, that means rule consists of more Item objects. so keep on parsing
        //if the node is a "output" node, that means parsing of rule options is complete. get the result and get out.
        static void parseDTXML(XmlNode node, List<Item> itemList, int order)
        {
            if (node.Name == "test")
            {
                XmlAttributeCollection attrList = node.Attributes;
                string attribute = attrList[0].Value;
                string value = attrList[2].Value;

                Item temp = new Item(attribute, value);
                itemList.Add(temp);

                for (int a = 0; a < node.ChildNodes.Count; a++)
                {
                    parseDTXML(node.ChildNodes[a], itemList, order);
                }
            }
            else if (node.Name == "output")
            {
                string result = node.Attributes[0].Value;

                Rule temp = new Rule(result, itemList);

                if (result != "p")
                {
                    TESTCASE_LIST[order].addRule(temp);
                }
            }

            if (itemList.Count > 1)
                itemList.RemoveAt(itemList.Count - 1);
        }
        
        //Given a list of items and an item, check if that item is in that list
        static bool doesExist(List<Item> list, Item obj)
        {
            string name = obj.getObjectName();
            string value = obj.getObjectValue();

            for (int counter = 0; counter < list.Count; counter++)
            {
                if (list[counter].getObjectName() == name)
                    if (list[counter].getObjectValue() == value)
                        return true;
            }
            return false;
        }

        //Given a configuration, checks if this configuration passes based on the rule list
        static bool doesThisConfigPass(Configuration param1, int order)
        {
            Configuration testingConfig = new Configuration();
            testingConfig.setEqualTo(param1);

            List<Item> optionsList = testingConfig.getItemList();

            for (int counter = 0; counter < TESTCASE_LIST[order].getRuleList().Count; counter++)
            {
                Rule tempRule = new Rule();
                tempRule.setEqualTo(TESTCASE_LIST[order].getRuleList()[counter]);
                List<Item> ruleOptionList = tempRule.getItemList();

                bool thereIsError = true;

                for (int a = 0; a < ruleOptionList.Count; a++)
                {
                    string optionName = ruleOptionList[a].getObjectName();
                    string optionValue = ruleOptionList[a].getObjectValue();

                    Item dummy = new Item(optionName, optionValue);

                    if (!doesExist(optionsList, dummy))
                    {
                        thereIsError = false;
                        break;
                    }
                }

                if (thereIsError)
                    return false;
            }
            return true;
        }

        //Given an option name, return the list of all values that option can take
        static List<string> getAllValues(string objName)
        {
            for (int a = 0; a < OPTION_LIST.Count; a++)
            {
                if (OPTION_LIST[a].getOptionName() == objName)
                    return OPTION_LIST[a].getValueList();
            }
            return null;
        }

        //Given an option name, return the number of different values that option can take
        static int howManyValues(string objName)
        {
            return (getAllValues(objName)).Count;
        }

        //Given a list of Item objects, return all subsets of the options in that list
        //the number of items in the resulting list will be 2^n - 1
        //input = [a,b,c]
        //result = [[a], [b], [c], [a,b], [a,c], [b,c] , [a,b,c]]
        static List<List<string>> getSubset(List<Item> input)
        {
            List<string> nameList = new List<string>();
            for (int a = 0; a < input.Count; a++)
            {
                string temp = input[a].getObjectName();
                nameList.Add(temp);
            }

            List<List<string>> result = new List<List<string>>();

            int level;

            for (int counter = 0; counter < nameList.Count; counter++)
            {
                level = (int)Math.Pow(2.0, (double)counter);
                string addThat = nameList[counter];

                List<string> oneElementOnly = new List<string>();
                oneElementOnly.Add(addThat);

                result.Add(oneElementOnly);

                for (int a = 0; a < level - 1; a++)
                {
                    List<string> temp = result[a];
                    List<string> temp2 = new List<string>();
                    for (int x = 0; x < temp.Count; x++)
                        temp2.Add(temp[x]);

                    temp2.Add(addThat);
                    result.Add(temp2);
                }
            }

            result.Sort(delegate(List<string> a, List<string> b) { return a.Count.CompareTo(b.Count); });
            return result;
        }

        //Just like the upper function, but returns List<Item> items rather than List<string>
        static List<List<Item>> getSubsetOptions(List<Item> input)
        {
            List<List<Item>> result = new List<List<Item>>();
            int level;

            for (int counter = 0; counter < input.Count; counter++)
            {
                level = (int)Math.Pow(2.0, (double)counter);
                Item addThat = new Item();
                addThat.setEqualTo(input[counter]);

                List<Item> oneElementOnly = new List<Item>();
                oneElementOnly.Add(addThat);

                result.Add(oneElementOnly);

                for (int a = 0; a < level - 1; a++)
                {
                    List<Item> temp = result[a];
                    List<Item> temp2 = new List<Item>();
                    for (int x = 0; x < temp.Count; x++)
                    {
                        Item heho = new Item();
                        heho.setEqualTo(temp[x]);
                        temp2.Add(heho);
                    }
                    temp2.Add(addThat);
                    result.Add(temp2);
                }
            }
            return result;
        }

        //given a list of option names, calculate the number of possible combinations for that list items
        //input = [a,b,c]
        //result = N(a) * N(b) * N(c)
        static int totalPossibleCombinations(List<string> input)
        {
            int result = 1;

            for (int a = 0; a < input.Count; a++)
            {
                result *= howManyValues(input[a]);
            }

            return result;
        }

        //given a list of option names, give the total different combinations of the options in the input list
        //input=[a,b] and a=0,1 b=0,1
        //result= [[a=0,b=0] , [a=0,b=1] , [a=1,b=0] , [a=1,b=1]]
        static List<List<Item>> getTruthTable(List<string> input)
        {
            int totalNumberOfElements = totalPossibleCombinations(input);

            List<List<Item>> result = new List<List<Item>>();
            for (int h = 0; h < totalNumberOfElements; h++)
                result.Add(new List<Item>());

            int changeTime = 1;

            for (int x = 0; x < input.Count; x++)
            {
                string optionName = input[x];
                int numberOfValuesForThatOption = howManyValues(optionName);
                
                List<string> values = getAllValues(optionName);

                int currentVal = 0;

                for (int y = 0; y < totalNumberOfElements; )
                {
                    string addThat = values[currentVal];
                    for (int z = 0; z < changeTime; z++)
                    {
                        Item temp = new Item(optionName, addThat);
                        result[y].Add(temp);
                        y++;
                    }

                    currentVal++;
                    currentVal %= numberOfValuesForThatOption;
                }

                changeTime *= numberOfValuesForThatOption;
            }

            return result;
        }

        //given an initial config and a list of changes, apply each change to the configuration
        //originalConfig = [a=0, b=1, c=0]  and changeList = [a=1,b=0]
        //result = [a=1, b=0, c=0]
        static Configuration applyChange(Configuration originalConfig, List<Item> changeList)
        {
            Configuration result = new Configuration();
            result.setEqualTo(originalConfig);

            for (int a = 0; a < changeList.Count; a++)
            {
                result.changeItemValue(changeList[a].getObjectName(), changeList[a].getObjectValue());
            }

            return result;
        }

        //returns the option list of the rule, that configuration is violating
        static List<Item> getRuleViolatingOptions(Configuration input, int order)
        {
            Configuration testingConfig = new Configuration();
            testingConfig.setEqualTo(input);

            List<Item> optionsList = testingConfig.getItemList();

            for (int counter = 0; counter < TESTCASE_LIST[order].getRuleList().Count; counter++)
            {
                Rule tempRule = new Rule();
                tempRule.setEqualTo(TESTCASE_LIST[order].getRuleList()[counter]);
                List<Item> ruleOptionList = tempRule.getItemList();

                bool thereIsError = true;

                for (int a = 0; a < ruleOptionList.Count; a++)
                {
                    string optionName = ruleOptionList[a].getObjectName();
                    string optionValue = ruleOptionList[a].getObjectValue();

                    Item dummy = new Item(optionName, optionValue);

                    if (!doesExist(optionsList, dummy))
                    {
                        thereIsError = false;
                        break;
                    }
                }

                if (thereIsError)
                {
                    List<Item> result = new List<Item>();
                    for (int a = 0; a < ruleOptionList.Count; a++)
                        result.Add(ruleOptionList[a]);
                    return result;
                }
            }
            return null;
        }

        //given a changed configuration, check if that configuration was in TRIPLE_LIST before
        static bool doesExistInScoreList(Configuration input)
        {
            for (int counter = 0; counter < TRIPLET_LIST.Count; counter++)
            {
                bool exists = true;

                Triplet tempTrip = new Triplet();
                tempTrip.setEqualTo(TRIPLET_LIST[counter]);

                List<Item> tripOptionList = tempTrip.getChangedConf().getItemList();
                List<Item> inputOptionList = input.getItemList();

                for (int a = 0; a < inputOptionList.Count; a++)
                {
                    if (!doesExist(tripOptionList, inputOptionList[a]))
                        exists = false;
                }

                if (exists)
                    return true;
            }
            return false;
        }

        //checks if the items in input list exists in any passing configuration
        static bool doWeHaveThisConfiguration(List<Item> input, int order)
        {
            for (int counter = 0; counter < TESTCASE_LIST[order].getPassingList().Count; counter++)
            {
                Configuration passConf = new Configuration();
                passConf.setEqualTo(TESTCASE_LIST[order].getPassingList()[counter]);

                List<Item> passOptions = passConf.getItemList();

                bool exists = true;

                for (int a = 0; a < input.Count; a++)
                {
                    if (!doesExist(passOptions, input[a]))
                        exists = false;
                }

                if (exists)
                    return true;
            }

            for (int counter = 0; counter < TESTCASE_LIST[order].getAddedList().Count; counter++)
            {
                Configuration passConf = new Configuration();
                passConf.setEqualTo(TESTCASE_LIST[order].getAddedList()[counter]);

                List<Item> passOptions = passConf.getItemList();

                bool exists = true;

                for (int a = 0; a < input.Count; a++)
                {
                    if (!doesExist(passOptions, input[a]))
                        exists = false;
                }

                if (exists)
                    return true;
            }
            
            return false;
        }

        static List<Item> getOptionsWithTheseNames(Configuration param1, List<string> names)
        {
            List<Item> result = new List<Item>();
            List<Item> itemList = param1.getItemList();

            for (int a = 0; a < names.Count; a++)
            {
                string nameToCheck = names[a];

                for (int b = 0; b < itemList.Count; b++)
                {
                    if (itemList[b].getObjectName() == nameToCheck)
                    {
                        Item temp = new Item();
                        temp.setEqualTo(itemList[b]);
                        result.Add(temp);
                    }
                }
            }
            return result;
        }

        static int calculateScore(Configuration input, int order)
        {
            int result = 0;

            List<string> failCoveringOptions = TESTCASE_LIST[order].getCoveringListOptions();
            List<Item> focusedItemList = getOptionsWithTheseNames(input, failCoveringOptions);

            List<List<Item>> subset = getSubsetOptions(focusedItemList);

            for (int subsetOrder = 0; subsetOrder < subset.Count; subsetOrder++)
            {
                if (!doWeHaveThisConfiguration(subset[subsetOrder], order))
                    result++;
            }

            return result;
        }

        static void updateTripletList(int order)
        {
            for (int counter = 0; counter < TRIPLET_LIST.Count; counter++)
            {
                Configuration temp = new Configuration();
                temp.setEqualTo(TRIPLET_LIST[counter].getChangedConf());

                int score = calculateScore(temp, order);

                TRIPLET_LIST[counter].setScore(score);
            }
        }

        //compares two lists of items
        //if they are equal, return true
        static bool areEqual(List<Item> a, List<Item> b)
        {
            if (a.Count != b.Count)
                return false;

            for (int counter = 0; counter < b.Count; counter++)
            {
                Item temp = new Item();
                temp.setEqualTo(b[counter]);

                if (!doesExist(a, temp))
                    return false;
            }

            return true;
        }
        
        //if b exists in a, returns the order of b in a
        //otherwise returns -1
        static int doesExist(List<List<Item>> a, List<Item> b)
        {
            for (int counter = 0; counter < a.Count; counter++)
            {
                if (areEqual(a[counter], b))
                    return counter;
            }
            return -1;
        }

        static void combineSet(List<List<Item>> a, List<List<Item>> b)
        {
            for (int counter = 0; counter < b.Count; counter++)
            {
                int location = doesExist(a, b[counter]);
                if (location == -1)
                {
                    List<Item> tempList = new List<Item>();
                    for (int xx = 0; xx < b[counter].Count; xx++)
                    {
                        Item temp = new Item();
                        temp.setEqualTo(b[counter][xx]);
                        tempList.Add(temp);
                    }
                    a.Add(tempList);
                }
            }
        }

        static void subtractSet(List<List<Item>> a, List<List<Item>> b)
        {
            for (int counter = 0; counter < b.Count; counter++)
            {
                int location = doesExist(a, b[counter]);
                if (location > -1)
                {
                    a.RemoveAt(location);
                }
            }
        }

        static void daErmanAlgorithm()
        {
            for (int TestOrder = 0; TestOrder < TESTCASE_LIST.Count; TestOrder++)
            {
                for (int orderOfFailingConfig = 0; orderOfFailingConfig < TESTCASE_LIST[TestOrder].getFailingList().Count; orderOfFailingConfig++)
                {
                    Configuration originalFailingConfiguration = new Configuration();
                    originalFailingConfiguration.setEqualTo(TESTCASE_LIST[TestOrder].getFailingList()[orderOfFailingConfig]);

                    bool passingConfigFound = false;

                    List<Item> ruleViolatingOptions = getRuleViolatingOptions(originalFailingConfiguration, TestOrder);

                    List<List<string>> subsetOfFailingOptions = getSubset(ruleViolatingOptions);

                    for (int subsetOrder = 0; (subsetOrder < subsetOfFailingOptions.Count) && !passingConfigFound; subsetOrder++)
                    {
                        List<List<Item>> changeList = getTruthTable(subsetOfFailingOptions[subsetOrder]);

                        for (int changeOrder = 0; changeOrder < changeList.Count; changeOrder++)
                        {
                            Configuration changedConfig = applyChange(originalFailingConfiguration, changeList[changeOrder]);
                            bool configPasses = doesThisConfigPass(changedConfig, TestOrder);

                            if (configPasses)
                            {
                                changedConfig.setResult("p");
                                TESTCASE_LIST[TestOrder].addNewConfiguration(changedConfig);
                                Console.Write("**old**\t");
                                print(originalFailingConfiguration);
                                Console.Write("**new**\t");
                                print(changedConfig);
                                Console.Write("\n");
                                passingConfigFound = true;
                                break;
                            }
                        }
                    }
                }
            }            
        }

        static void daErdalAlgorithm()
        {
            for (int TestOrder = 0; TestOrder < TESTCASE_LIST.Count; TestOrder++)
            {
                for (int orderOfFailingConfig = 0; orderOfFailingConfig < TESTCASE_LIST[TestOrder].getFailingList().Count; orderOfFailingConfig++)
                {
                    Configuration originalFailingConfig = new Configuration();
                    originalFailingConfig.setEqualTo(TESTCASE_LIST[TestOrder].getFailingList()[orderOfFailingConfig]);

                    List<Item> ruleViolatingOptions = getRuleViolatingOptions(originalFailingConfig,TestOrder);

                    if (ruleViolatingOptions != null)
                    {
                        List<List<string>> subsetOfFailingOptions = getSubset(ruleViolatingOptions);

                        for (int subsetOrder = 0; subsetOrder < subsetOfFailingOptions.Count; subsetOrder++)
                        {
                            List<List<Item>> changeList = getTruthTable(subsetOfFailingOptions[subsetOrder]);
                            for (int changeOrder = 0; changeOrder < changeList.Count; changeOrder++)
                            {
                                Configuration changedConfig = applyChange(originalFailingConfig, changeList[changeOrder]);
                                bool configPasses = doesThisConfigPass(changedConfig, TestOrder);

                                if (configPasses)
                                {
                                    if (!doesExistInScoreList(changedConfig))
                                    {
                                        int score = calculateScore(changedConfig, TestOrder);
                                        if (score > 0)
                                        {
                                            Triplet tr = new Triplet(originalFailingConfig, changedConfig, score);
                                            TRIPLET_LIST.Add(tr);
                                        }
                                    }
                                }
                            }
                        }
                    }                    

                    TRIPLET_LIST.Sort(delegate(Triplet a, Triplet b) { return a.getScore().CompareTo(b.getScore()); });

                    if (TRIPLET_LIST.Count > 0)
                    {
                        Configuration toAdd = new Configuration();
                        toAdd.setEqualTo(TRIPLET_LIST[TRIPLET_LIST.Count - 1].getChangedConf());
                        Configuration orig = new Configuration();
                        orig.setEqualTo(TRIPLET_LIST[TRIPLET_LIST.Count - 1].getOriginalConf());
                                               

                        toAdd.setResult("p");
                        TESTCASE_LIST[TestOrder].addNewConfiguration(toAdd);

                        Console.Write("**old**\t");
                        print(orig);
                        Console.Write("**new**\t");
                        print(toAdd);
                        Console.Write("\n");

                        TRIPLET_LIST.RemoveAt(TRIPLET_LIST.Count - 1);

                        if (CHOOSE_GLOBAL)
                        {
                            updateTripletList(TestOrder);
                        }
                        else
                        {
                            TRIPLET_LIST.Clear();
                        }
                    }                
                }

                TRIPLET_LIST.Clear();
            }           
        }

        static int numberOfElements(List<List<Item>> a, int order)
        {
            int result = 0;

            for (int x = 0; x < a.Count; x++)
                if (a[x].Count == order)
                    result++;
            return result;
        }

        static void calculateAlgorithmScore()
        {
            TextWriter tw = new StreamWriter("Score.txt");

            for (int TestOrder = 0; TestOrder < TESTCASE_LIST.Count; TestOrder++)
            {
                List<List<Item>> totalSubset = new List<List<Item>>();

                for (int count = 0; count < TESTCASE_LIST[TestOrder].getAddedList().Count; count++)
                {
                    Configuration tempCof = new Configuration();
                    tempCof.setEqualTo(TESTCASE_LIST[TestOrder].getAddedList()[count]);

                    List<string> failureCoveringOptions = TESTCASE_LIST[TestOrder].getCoveringListOptions();
                    List<Item> focusedOptionList = getOptionsWithTheseNames(tempCof, failureCoveringOptions);

                    combineSet(totalSubset, getSubsetOptions(focusedOptionList));
                }

                for (int count2 = 0; count2 < TESTCASE_LIST[TestOrder].getPassingList().Count; count2++)
                {
                    Configuration tempCof2 = new Configuration();
                    tempCof2.setEqualTo(TESTCASE_LIST[TestOrder].getPassingList()[count2]);

                    List<string> failureCoveringOptions2 = TESTCASE_LIST[TestOrder].getCoveringListOptions();
                    List<Item> focusedOptionList2 = getOptionsWithTheseNames(tempCof2, failureCoveringOptions2);

                    subtractSet(totalSubset, getSubsetOptions(focusedOptionList2));
                }

                totalSubset.Sort(delegate(List<Item> a, List<Item> b) { return a.Count.CompareTo(b.Count); });

                TESTCASE_LIST[TestOrder].setScore(totalSubset.Count);

                tw.WriteLine("Test_ID= " + TESTCASE_LIST[TestOrder].getId() + "\t" +
                         "Number of new configurations=" + TESTCASE_LIST[TestOrder].getAddedList().Count + "\t" +
                         "Number of new combinations found=" + TESTCASE_LIST[TestOrder].getScore());
            }
            tw.Close();
        }

        static void print(Configuration param1)
        {
            string result = param1.getResult();
            List<Item> options = param1.getItemList();

            Console.Write("result=" + result + " ");

            for (int a = 0; a < options.Count; a++)
                Console.Write(options[a].getObjectName() + "=" + options[a].getObjectValue() + " ");

            Console.Write("\n");
        }

        static void printCsvOutput()
        {
            for (int a = 0; a < TESTCASE_LIST.Count; a++)
            {
                string filename = "newConfigFor"+TESTCASE_LIST[a].getId()+".csv";
                TextWriter tw = new StreamWriter(filename);
                List<Configuration> passList = TESTCASE_LIST[a].getPassingList();
                List<Configuration> addList = TESTCASE_LIST[a].getAddedList();

                for (int x = 0; x < OPTION_LIST.Count; x++)
                {
                    tw.Write(OPTION_LIST[x].getOptionName() + ",");
                }
                tw.Write("\n");


                //print passing configurations
                for (int x = 0; x < passList.Count; x++)
                {
                    List<Item> itemList = passList[x].getItemList();
                    for (int y = 0; y < itemList.Count; y++)
                    {
                        tw.Write(itemList[y].getObjectValue() + ",");
                    }
                    tw.Write("\n");
                }

                //print added configurations
                for (int x = 0; x < addList.Count; x++)
                {
                    List<Item> itemList = addList[x].getItemList();
                    for (int y = 0; y < itemList.Count; y++)
                    {
                        tw.Write(itemList[y].getObjectValue() + ",");
                    }
                    tw.Write("\n");
                }
                tw.Close();
            }
        }

        static void Main(string[] args)
        {
            //args is
            //"options file"+"configurationbase file"+["decisiontree file"]+"algorithmname"+"global choose"

            if (args.Length < 4)
                return;

            string optionFileName = args[0];
            string configurationFileName = args[1];
            
            List<string> decisionTreeFiles = new List<string>();
            string decisionFile = args[2];
            int i = 2;

            while (decisionFile.EndsWith(".xml"))
            {
                decisionTreeFiles.Add(decisionFile);

                i++;
                decisionFile = args[i];
            }

            string algorithmName = args[i];
            i++;

            string isGlobal = "";
            if (args.Length > i)
                isGlobal = args[i];
            
            parseOptionsXML(optionFileName);
            parseConfigurationsXML(configurationFileName);
            for ( int a = 0; a<decisionTreeFiles.Count; a++ )
                parseDecisionTreeXML(decisionTreeFiles[a]);
            

            if (isGlobal == "local")
                CHOOSE_GLOBAL = false;
            else if (isGlobal == "global")
                CHOOSE_GLOBAL = true;
            else
                CHOOSE_GLOBAL = false;


            if (algorithmName == "first")
                daErmanAlgorithm();
            else if (algorithmName == "optimal")
                daErdalAlgorithm();
            else
                return;
            calculateAlgorithmScore();

            printCsvOutput();
        }
    }
}
