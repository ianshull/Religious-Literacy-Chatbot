import random

def Christian_Opinions():
  dict= {
      #Demographic Information

      "Age distribution among Christians": "Percent of Christians who are ages: 18-29- 17%, 30-49- 33%, 50-64- 29%, 65+ - 21%",
      "Generational cohort among Christians": "Percent of Christians who are: Younger Millenial- 11%, Older Millenial- 12%, Generation X- 28%, Baby Boomer- 35%, Silent- 14%, Greatest- 1%",
      "Gender composition among Christians":"Percent of Christians who are: Men- 45%, Women- 55%",
      "Racial and ethnic composition among Christians":"Percent of Christians who identify as: White- 66%, LatinX- 16%, Black- 13%, Asian- 2%, Other- 3%",
      "Immigrant status among Christians": "Percent of Christians who are: Immigrants- 14%, Second generation- 9%, Third generation or higher- 77%",
      "Income distribution among Christians": "Percent of Christians who have a household income of: Less than $30,000- 36%, $30,000-$49,999- 21%, $50,000-$99,999- 27%, $100,000 or more- 17%",
      "Educational distribution among Christians": "Percent of Christians who have completed: High school or less- 43%, Some college- 32%, College- 16%, Post-graduate degree- 9%",
      "Marital status among Christians": "Percent of Christians who are: Married- 52%, Living with a partner- 6%, Divorced/sparated- 14%, Widowed- 8%, Never married- 21%",
      "Parent of children under 18 among Christians": "Percent of Christians who are: Parents- 30%, Non-parents- 70%",
      
      #Beliefs And Practices

      "Belief in God among Christians": "Percent of Christians who say they: Believe in God; absolutely- 76%, Believe in God; fairly certain- 18%, Believe in God; not too/not at all certain- 3%, Believe in God; don't know- 1%, Do not believe in God- 1%, Other/don't know if they believe in God- 1%",
      "Importance of religion in one's life among Christians": "Percent of Christians who say religion is: Very important- 68%, Somewhat Important- 25%, Not too important- 5%, Not at all important- 2%, Don't know- 1%",
      "Attendance at religious services among Christians": "Percent of Christians who attend religious services: At least once a week- 47%, Once or twice a month/a few times a year- 36%, Seldom/never- 17%, Don't know- 1%",
      "Frequency of prayer among Christians": "Percent of Christians who pray: At least daily- 68%, Weekly- 17%, Monthly- 5%, Seldom/never- 9%, Don't know- 1%",
      "Frequency of participation in prayer, scripture study or religious education groups among Christians": "Percent of Christians who attend prayer group: At least once a week- 32%, Once or twice a month- 11%, Several times a year- 9%, Seldom/never- 47%, Don't know- 1%",
      "Frequency of meditation among Christians": "Percent of Christians who meditate: At least once a week- 45%, Once or twice a month- 8%, Several times a year- 4%, Seldom/never- 41%, Don't know- 2%",
      "Frequency of feeling spiritual peace and wellbeing among Christians": "Percent of Christians who feel a sense of spiritual peace and wellbeing: At least once a week- 65%, Once or twice a month- 14%, Several times a year- 9%, Seldom/never- 10%, Don't know- 1% ",
      "Frequency of feeling wonder about the universe among Christians": "Percent of Christians who feel a sense of wonder about the universe: At least once a week- 45%, Once or twice a month- 16%, Several times a year- 13%, Seldom/never- 25%, Don't know- 2%",
      "Sources of guidance on right and wrong among Christians": "Percent of Christians who say they look to…most for guidance on right and wrong: Religion- 43%, Philosophy/reason- 8%, Common sense- 41%, Science- 6%, Don't know- 2%",
      "Belief in absolute standards for right and wrong among Christians": "Percent of Christians who say: There are clear standards for what is right and wrong- 38%, Right or wrong depends on the situation- 59%, Neither/both equally- 1%, Don't know- 1%",
      "Frequency of reading scripture among Christians": "Percent of Christians who read scripture: At least once a week- 45%, Once or twice a month- 12%, Several times a year- 9%, Seldom/never- 33%, Don't know- 1%",
      "Interpreting scripture among Christians": "Percent of Christians who say the holy scripture is: Word of God; should be taken literally- 39%, Word of God; not everything taken literally- 33%, Word of God; other/don't know- 3%, Not the word of God- 18%, Other/don't know- 7%",
      "Belief in Heaven among Christians":"Percent of Christians who…in heaven: Believe- 85%, Don't believe- 8%, Other/don't know- 6%",
      "Belief in Hell among Christians": "Percent of Christians who …in hell: Believe- 70%, Don't believe- 22%, Other/don't know- 8%",
      
      #Social And Political Views
      
      "Party affiliation among Christians": "Percent of Christians who identify as: Republicam/lean Rep.- 43%, No lean- 17%, Democrat/lean Dem.- 40%",
      "Political ideology among Christians": "Percent of Christians who are: Conservative- 44%, Moderate- 32%, Liberal- 18%, Don't know- 6%",
      "Views about size of government among Christians": "Percent of Christians who would rather have: Smaller government; fewer services- 54%, Bigger government; more services- 39%, Depends- 3%,Don't know- 4%",
      "Views about government aid to the poor among Christians": "Percent of Christians who say government aid to the poor: Does more harm than good- 49%, Does more good than harm- 46%, Neither/both equally- 4%, Don't know- 2%",
      "Views about abortion among Christians": "Percent of Christians who say abortion should be: Legal in all/most cases- 45%, Illegal in all/most cases- 51%, Don't know- 4%",
      "Views about homosexuality among Christians": "Percent of Christians who say homosexuality: Should be accepted- 54%, Should be discouraged- 38%, Neither/both equally- 4%, Don't know- 4%",
      "Views about same-sex marriage among Christians": "Percent of Christians who …same-sex marriage: Strongly favor/favor- 44%, Oppose/strongly oppose- 48%, Don't know- 8%",
      "Views about environmental regulation among Christians": "Percent of Christians who say: Stricter environmental laws and regulations cost too many jobs and hurt the economy- 42%, Stricter environmnetal laws and regulations are worth the cost- 52%, Neither/both equally- 2%, Don't know- 3%",
      "Views about human evolution among Christians": "Percent of Christians who say humans: Evolved; due to natural process- 21%, Evolved; due to God's design- 29%, Evolved; don't know how- 4%, Always exsited in present form- 42%, Don't know- 5%"

      #source: https://www.pewforum.org/religious-landscape-study/christians/christian/


  }
  print(random.choice(list(dict.values())))
  
def Judaism_Opinions():
    dict= {
      #Demographic Information

      "Age distribution among Jews": "Percent of Jews who are ages: 18-29- 22%, 30-49- 27%, 50-64- 26%, 65+ - 26%",
      "Generational cohort among Jews": "Percent of Jews who are: Younger Millenial- 13%, Older Millenial- 13%, Generation X- 23%, Baby Boomer- 33%, Silent- 15%, Greatest- 3%",
      "Gender composition among Jews":"Percent of Jews who are: Men- 52%, Women- 48%",
      "Racial and ethnic composition among Jews":"Percent of Jews who identify as: White- 90%, Black- 2%, Asian- 2%, LatinX- 4%, Other- 3%",
      "Immigrant status among Jews": "Percent of Jews who are: Immigrants- 12%, Second generation- 22%, Third generation or higher- 67%",
      "Income distribution among Jews": "Percent of Jews who have a household income of: Less than $30,000- 16%, $30,000-$49,999- 15%, $50,000-$99,999- 24%, $100,000 or more- 44%",
      "Educational distribution among Jews": "Percent of Jews who have completed: High school or less- 19%, Some college- 22%, College- 29%, Post-graduate degree- 31%",
      "Marital status among Jews": "Percent of Jews who are: Married- 56%, Living with a partner- 6%, Divorced/sparated- 9%, Widowed- 6%, Never married- 23%",
      "Parent of children under 18 among Jews": "Percent of Jews who are: Parents- 26%, Non-parents- 74%",
      
      #Beliefs And Practices

      "Belief in God among Jews": "Percent of Jews who say they: Believe in God; absolutely- 37%, Believe in God; fairly certain- 27%, Believe in God; not too/not at all certain- 14%, Believe in God; don't know- 1%, Do not believe in God- 17%, Other/don't know if they believe in God- 4%",
      "Importance of religion in one's life among Jews": "Percent of Jews who say religion is: Very important- 35%, Somewhat Important- 36%, Not too important- 20%, Not at all important- 9%, Don't know- <1%",
      "Attendance at religious services among Jews": "Percent of Jews who attend religious services: At least once a week- 19%, Once or twice a month/a few times a year- 49%, Seldom/never- 31%, Don't know- <1%",
      "Frequency of prayer among Jews": "Percent of Jews who pray: At least daily- 29%, Weekly- 16%, Monthly- 8%, Seldom/never- 45%, Don't know- 1%",
      "Frequency of participation in prayer, scripture study or religious education groups among Jews": "Percent of Jews who attend prayer group: At least once a week- 16%, Once or twice a month- 9%, Several times a year- 11%, Seldom/never- 62%, Don't know- 1%",
      "Frequency of meditation among Jews": "Percent of Jews who meditate: At least once a week- 28%, Once or twice a month- 8%, Several times a year- 6%, Seldom/never- 56%, Don't know- 2%",
      "Frequency of feeling spiritual peace and wellbeing among Jews": "Percent of Jews who feel a sense of spiritual peace and wellbeing: At least once a week- 39%, Once or twice a month- 18%, Several times a year- 14%, Seldom/never- 28%, Don't know- 1% ",
      "Frequency of feeling wonder about the universe among Jews": "Percent of Jews who feel a sense of wonder about the universe: At least once a week- 42%, Once or twice a month- 18%, Several times a year- 15%, Seldom/never- 23%, Don't know- 1%",
      "Sources of guidance on right and wrong among Jews": "Percent of Jews who say they look to…most for guidance on right and wrong: Religion- 17%, Philosophy/reason- 17%, Common sense- 50%, Science- 14%, Don't know- 3%",
      "Belief in absolute standards for right and wrong among Jews": "Percent of Jews who say: There are clear standards for what is right and wrong- 21%, Right or wrong depends on the situation- 76%, Neither/both equally- 2%, Don't know- 1%",
      "Frequency of reading scripture among Jews": "Percent of Jews who read scripture: At least once a week- 17%, Once or twice a month- 8%, Several times a year- 9%, Seldom/never- 65%, Don't know- 1%",
      "Interpreting scripture among Jews": "Percent of Jews who say the holy scripture is: Word of God; should be taken literally- 11%, Word of God; not everything taken literally- 24%, Word of God; other/don't know- 2%, Not the word of God- 55%, Other/don't know- 8%",
      "Belief in Heaven among Jews":"Percent of Jews who…in heaven: Believe- 40%, Don't believe- 49%, Other/don't know- 11%",
      "Belief in Hell among Jews": "Percent of Jews who …in hell: Believe- 22%, Don't believe- 70%, Other/don't know- 7%",
      
      #Social And Political Views
      
      "Party affiliation among Jews": "Percent of Jews who identify as: Republicam/lean Rep.- 26%, No lean- 9%, Democrat/lean Dem.- 64%",
      "Political ideology among Jews": "Percent of Jews who are: Conservative- 21%, Moderate- 33%, Liberal- 43%, Don't know- 3%",
      "Views about size of government among Jews": "Percent of Jews who would rather have: Smaller government; fewer services- 40%, Bigger government; more services- 53%, Depends-4%, Don't know- 3%",
      "Views about government aid to the poor among Jews": "Percent of Jews who say government aid to the poor: Does more harm than good- 29%, Does more good than harm- 65%, Neither/both equally- 3%, Don't know- 3%",
      "Views about abortion among Jews": "Percent of Jews who say abortion should be: Legal in all/most cases- 83%, Illegal in all/most cases- 15%, Don't know- 2%",
      "Views about homosexuality among Jews": "Percent of Jews who say homosexuality: Should be accepted- 81%, Should be discouraged- 16%, Neither/both equally- 2%, Don't know- 1%",
      "Views about same-sex marriage among Jewss": "Percent of Jews who …same-sex marriage: Strongly favor/favor- 77%, Oppose/strongly oppose- 18%, Don't know- 5%",
      "Views about environmental regulation among Jews": "Percent of Jews who say: Stricter environmental laws and regulations cost too many jobs and hurt the economy- 25%, Stricter environmnetal laws and regulations are worth the cost- 71%, Neither/both equally- 2%, Don't know- 2%",
      "Views about human evolution among Jews": "Percent of Jews who say humans: Evolved; due to natural process- 58%, Evolved; due to God's design- 18%, Evolved; don't know how- 5%, Always exsited in present form- 16%, Don't know- 3%"

      #source: https://www.pewforum.org/religious-landscape-study/religious-tradition/jewish/
    }
    print(random.choice(list(dict.values())))
    
def Hinduism_Opinions():
    dict= {
      #Demographic Information

      "Age distribution among Hindus": "Percent of Hindus who are ages: 18-29- 34%, 30-49- 56%, 50-64- 6%, 65+ - 4%",
      "Generational cohort among Hindus": "Percent of Hindus who are: Younger Millenial- 14%, Older Millenial- 36%, Generation X- 40%, Baby Boomer- 8%, Silent- 1%, Greatest- <1%",
      "Gender composition among Hindus":"Percent of Hindus who are: Men- 62%, Women- 38%",
      "Racial and ethnic composition among Hindus":"Percent of Hindus who identify as: White- 4%, Black- 2%, Asian- 91%, LatinX- 1%, Other- 2%",
      "Immigrant status among Hindus": "Percent of Hindus who are: Immigrants- 87%, Second generation- 9%, Third generation or higher- 4%",
      "Income distribution among Hindus": "Percent of Hindus who have a household income of: Less than $30,000- 17%, $30,000-$49,999- 13%, $50,000-$99,999- 34%, $100,000 or more- 36%",
      "Educational distribution among Hindus": "Percent of Hindus who have completed: High school or less- 12%, Some college- 11%, College- 29%, Post-graduate degree- 48%",
      "Marital status among Hindus": "Percent of Hindus who are: Married- 60%, Living with a partner- 3%, Divorced/sparated- 5%, Widowed- 1%, Never married- 32%",
      "Parent of children under 18 among Hindus": "Percent of Hindus who are: Parents- 39%, Non-parents- 61%",
      
      #Beliefs And Practices

      "Belief in God among Hindus": "Percent of Hindus who say they: Believe in God; absolutely- 41%, Believe in God; fairly certain- 34%, Believe in God; not too/not at all certain- 13%, Believe in God; don't know- 1%, Do not believe in God- 10%, Other/don't know if they believe in God- 2%",
      "Importance of religion in one's life among Hindus": "Percent of Hindus who say religion is: Very important- 26%, Somewhat Important- 53%, Not too important- 15%, Not at all important- 6%, Don't know- <1%",
      "Attendance at religious services among Hindus": "Percent of Hindus who attend religious services: At least once a week- 18%, Once or twice a month/a few times a year- 60%, Seldom/never- 21%, Don't know- 1%",
      "Frequency of prayer among Hindus": "Percent of Hindus who pray: At least daily- 51%, Weekly- 15%, Monthly- 12%, Seldom/never- 22%, Don't know- 1%",
      "Frequency of participation in prayer, scripture study or religious education groups among Hindus": "Percent of Hindus who attend prayer group: At least once a week- 9%, Once or twice a month- 13%, Several times a year- 21%, Seldom/never- 57%, Don't know- <1%",
      "Frequency of meditation among Hindus": "Percent of Hindus who meditate: At least once a week- 33%, Once or twice a month- 8%, Several times a year- 7%, Seldom/never- 51%, Don't know- <1%",
      "Frequency of feeling spiritual peace and wellbeing among Hindus": "Percent of Hindus who feel a sense of spiritual peace and wellbeing: At least once a week- 40%, Once or twice a month- 16%, Several times a year- 22%, Seldom/never- 20%, Don't know- 2% ",
      "Frequency of feeling wonder about the universe among Hindus": "Percent of Hindus who feel a sense of wonder about the universe: At least once a week- 33%, Once or twice a month- 20%, Several times a year- 26%, Seldom/never- 21%, Don't know- <1%",
      "Sources of guidance on right and wrong among Hindus": "Percent of Hindus who say they look to…most for guidance on right and wrong: Religion- 6%, Philosophy/reason- 19%, Common sense- 50%, Science- 24%, Don't know- 1%",
      "Belief in absolute standards for right and wrong among Hindus": "Percent of Hindus who say: There are clear standards for what is right and wrong- 20%, Right or wrong depends on the situation- 78%, Neither/both equally- 1%, Don't know- 1%",
      "Frequency of reading scripture among Hindus": "Percent of Hindus who read scripture: At least once a week- 10%, Once or twice a month-11%, Several times a year- 18%, Seldom/never- 60%, Don't know- 1%",
      "Interpreting scripture among Hindus": "Percent of Hindus who say the holy scripture is: Word of God; should be taken literally- 12%, Word of God; not everything taken literally- 16% Word of God; other/don't know- <1%, Not the word of God- 60%, Other/don't know- 12%",
      "Belief in Heaven among Hindus":"Percent of Hindus who…in heaven: Believe- 48%, Don't believe- 42%, Other/don't know- 9%",
      "Belief in Hell among Hindus": "Percent of Hindus who …in hell: Believe- 28%, Don't believe- 62%, Other/don't know- 11%",
      
      #Social And Political Views
      
      "Party affiliation among Hindus": "Percent of Hindus who identify as: Republicam/lean Rep.- 13%, No lean- 26%, Democrat/lean Dem.- 61%",
      "Political ideology among Hindus": "Percent of Hindus who are: Conservative- 14%, Moderate- 38%, Liberal- 43%, Don't know- 4%",
      "Views about size of government among Hindus": "Percent of Hindus who would rather have: Smaller government; fewer services- 40%, Bigger government; more services- 57%, Depends- 4%, Don't know- <1%",
      "Views about government aid to the poor among Hindus": "Percent of Hindus who say government aid to the poor: Does more harm than good- 33%, Does more good than harm- 58%, Neither/both equally- 7%, Don't know- 3%",
      "Views about abortion among Hindus": "Percent of Hindus who say abortion should be: Legal in all/most cases- 68%, Illegal in all/most cases- 29%, Don't know- 3%",
      "Views about homosexuality among Hindus": "Percent of Hindus who say homosexuality: Should be accepted- 71%, Should be discouraged- 22%, Neither/both equally- 5%, Don't know- 2%",
      "Views about same-sex marriage among Hindus": "Percent of Hindus who …same-sex marriage: Strongly favor/favor- 68%, Oppose/strongly oppose- 23%, Don't know- 9%",
      "Views about environmental regulation among Hindus": "Percent of Hindus who say: Stricter environmental laws and regulations cost too many jobs and hurt the economy- 26%, Stricter environmnetal laws and regulations are worth the cost- 69%, Neither/both equally- 2%, Don't know- 3%",
      "Views about human evolution among Hindus": "Percent of Hindus who say humans: Evolved; due to natural process- 62%, Evolved; due to God's design- 14%, Evolved; don't know how- 3%, Always exsited in present form- 17%, Don't know- 3%"

      #source: https://www.pewforum.org/religious-landscape-study/religious-tradition/hindu/
    }
    print(random.choice(list(dict.values())))

    
def Mormon_Opinions():
    dict= {
      #Demographic Information

      "Age distribution among Mormons": "Percent of Mormons who are ages: 18-29- 22%, 30-49- 40%, 50-64- 22%, 65+ - 16%",
      "Generational cohort among Mormons": "Percent of Mormons who are: Younger Millenial- 14%, Older Millenial- 17%, Generation X- 31%, Baby Boomer- 26%, Silent- 11%, Greatest- 1%",
      "Gender composition among Mormons":"Percent of Mormons who are: Men- 46%, Women- 54%",
      "Racial and ethnic composition among Mormons":"Percent of Mormons who identify as: White- 85%, Black- 1%, Asian- 1%, LatinX- 8%, Other- 5%",
      "Immigrant status among Mormons": "Percent of Mormons who are: Immigrants- 7%, Second generation- 7%, Third generation or higher- 86%",
      "Income distribution among Mormons": "Percent of Mormons who have a household income of: Less than $30,000- 27%, $30,000-$49,999- 20%, $50,000-$99,999- 33%, $100,000 or more- 20%",
      "Educational distribution among Mormons": "Percent of Mormons who have completed: High school or less- 27%, Some college- 40%, College- 23%, Post-graduate degree- 10%",
      "Marital status among Mormons": "Percent of Mormons who are: Married- 66%, Living with a partner- 3%, Divorced/sparated- 7%, Widowed- 5%, Never married- 19%",
      "Parent of children under 18 among Mormons": "Percent of Mormons who are: Parents- 41%, Non-parents- 59%",
      
      #Beliefs And Practices

      "Belief in God among Mormons": "Percent of Mormons who say they: Believe in God; absolutely- 86%, Believe in God; fairly certain- 11%, Believe in God; not too/not at all certain- 2%, Believe in God; don't know- <1%, Do not believe in God- <1%, Other/don't know if they believe in God- 1%",
      "Importance of religion in one's life among Mormons": "Percent of Mormons who say religion is: Very important- 84%, Somewhat Important- 12%, Not too important- 3%, Not at all important- 1%, Don't know- <1%",
      "Attendance at religious services among Mormons": "Percent of Mormons who attend religious services: At least once a week- 77%, Once or twice a month/a few times a year- 14%, Seldom/never- 9%, Don't know- 1%",
      "Frequency of prayer among Mormons": "Percent of Mormons who pray: At least daily- 85%, Weekly- 7%, Monthly- 3%, Seldom/never- 5%, Don't know- <1%",
      "Frequency of participation in prayer, scripture study or religious education groups among Mormons": "Percent of Mormons who attend prayer group: At least once a week- 71%, Once or twice a month- 7%, Several times a year- 3%, Seldom/never- 19%, Don't know- <1%",
      "Frequency of meditation among Mormons": "Percent of Mormons who meditate: At least once a week- 60%, Once or twice a month- 10%, Several times a year- 1%, Seldom/never- 28%, Don't know- 1%",
      "Frequency of feeling spiritual peace and wellbeing among Mormons": "Percent of Mormons who feel a sense of spiritual peace and wellbeing: At least once a week- 81%, Once or twice a month- 9%, Several times a year- 4%, Seldom/never- 5%, Don't know- 1% ",
      "Frequency of feeling wonder about the universe among Mormons": "Percent of Mormons who feel a sense of wonder about the universe: At least once a week- 49%, Once or twice a month- 23%, Several times a year- 13%, Seldom/never- 14%, Don't know- <1%",
      "Sources of guidance on right and wrong among Mormons": "Percent of Mormons who say they look to…most for guidance on right and wrong: Religion- 64%, Philosophy/reason- 4%, Common sense- 25%, Science- 4%, Don't know- 3%",
      "Belief in absolute standards for right and wrong among Mormons": "Percent of Mormons who say: There are clear standards for what is right and wrong- 57%, Right or wrong depends on the situation- 41%, Neither/both equally- 2%, Don't know- <1%",
      "Frequency of reading scripture among Mormons": "Percent of Mormons who read scripture: At least once a week- 77%, Once or twice a month- 7%, Several times a year- 3%, Seldom/never- 12%, Don't know- 1%",
      "Interpreting scripture among Mormons": "Percent of Mormons who say the holy scripture is: Word of God; should be taken literally- 33%, Word of God; not everything taken literally- 53% Word of God; other/don't know- 5%, Not the word of God- 6%, Other/don't know- 3%",
      "Belief in Heaven among Mormons":"Percent of Mormons who…in heaven: Believe- 95%, Don't believe- 2%, Other/don't know- 3%",
      "Belief in Hell among Mormons": "Percent of Mormons who …in hell: Believe- 62%, Don't believe- 30%, Other/don't know- 8%",
      
      #Social And Political Views
      
      "Party affiliation among Mormons": "Percent of Mormons who identify as: Republicam/lean Rep.- 70%, No lean- 11%, Democrat/lean Dem.- 19%",
      "Political ideology among Mormons": "Percent of Mormons who are: Conservative- 61%, Moderate- 27%, Liberal- 9%, Don't know- 4%",
      "Views about size of government among Mormons": "Percent of Mormons who would rather have: Smaller government; fewer services- 75%, Bigger government; more services- 22%, Depends- 2%, Don't know- 2%",
      "Views about government aid to the poor among Mormons": "Percent of Mormons who say government aid to the poor: Does more harm than good- 64%, Does more good than harm- 31%, Neither/both equally- 3%, Don't know- 1%",
      "Views about abortion among Mormons": "Percent of Mormons who say abortion should be: Legal in all/most cases- 27%, Illegal in all/most cases- 70%, Don't know- 2%",
      "Views about homosexuality among Mormons": "Percent of Mormons who say homosexuality: Should be accepted- 36%, Should be discouraged- 57%, Neither/both equally- 4%, Don't know- 3%",
      "Views about same-sex marriage among Mormons": "Percent of Mormons who …same-sex marriage: Strongly favor/favor- 26%, Oppose/strongly oppose- 68%, Don't know- 6%",
      "Views about environmental regulation among Mormons": "Percent of Mormons who say: Stricter environmental laws and regulations cost too many jobs and hurt the economy- 53%, Stricter environmnetal laws and regulations are worth the cost- 42%, Neither/both equally- 3%, Don't know- 2%",
      "Views about human evolution among Mormons": "Percent of Mormons who say humans: Evolved; due to natural process- 11%, Evolved; due to God's design- 29%, Evolved; don't know how- 2%, Always exsited in present form- 52%, Don't know- 7%"

      #source: https://www.pewforum.org/religious-landscape-study/religious-tradition/mormon/
    }
    print(random.choice(list(dict.values())))
   


def Muslim_Opinions():
    dict= {
      #Demographic Information

      "Age distribution among Muslims": "Percent of Muslims who are ages: 18-29- 44%, 30-49- 37%, 50-64- 13%, 65+ - 5%",
      "Generational cohort among Muslims": "Percent of Muslims who are: Younger Millenial- 29%, Older Millenial- 22%, Generation X- 31%, Baby Boomer- 15%, Silent- 4%, Greatest- <1%",
      "Gender composition among Muslims":"Percent of Muslims who are: Men- 65%, Women- 35%",
      "Racial and ethnic composition among Muslims":"Percent of Muslims who identify as: White- 38%, Black- 28%, Asian- 28%, LatinX- 4%, Other- 3%",
      "Immigrant status among Muslims": "Percent of Muslims who are: Immigrants- 64%, Second generation- 17%, Third generation or higher- 18%",
      "Income distribution among Muslims": "Percent of Muslims who have a household income of: Less than $30,000- 34%, $30,000-$49,999- 17%, $50,000-$99,999- 29%, $100,000 or more- 20%",
      "Educational distribution among Muslims": "Percent of Muslims who have completed: High school or less- 36%, Some college- 25%, College- 23%, Post-graduate degree- 17%",
      "Marital status among Muslims": "Percent of Muslims who are: Married- 41%, Living with a partner- 4%, Divorced/sparated- 8%, Widowed- 1%, Never married- 45%",
      "Parent of children under 18 among Muslims": "Percent of Muslims who are: Parents- 38%, Non-parents- 62%",
      
      #Beliefs And Practices

      "Belief in God among Muslims": "Percent of Muslims who say they: Believe in God; absolutely- 84%, Believe in God; fairly certain- 12%, Believe in God; not too/not at all certain- 3%, Believe in God; don't know- <1%, Do not believe in God- 1%, Other/don't know if they believe in God- <1%",
      "Importance of religion in one's life among Muslims": "Percent of Muslims who say religion is: Very important- 64%, Somewhat Important- 24%, Not too important- 8%, Not at all important- 2%, Don't know- 1%",
      "Attendance at religious services among Muslims": "Percent of Muslims who attend religious services: At least once a week- 45%, Once or twice a month/a few times a year- 31%, Seldom/never- 22%, Don't know- 1%",
      "Frequency of prayer among Muslims": "Percent of Muslims who pray: At least daily- 69%, Weekly- 9%, Monthly- 7%, Seldom/never- 13%, Don't know- 1%",
      "Frequency of participation in prayer, scripture study or religious education groups among Muslims": "Percent of Muslims who attend prayer group: At least once a week- 35%, Once or twice a month- 10%, Several times a year- 14%, Seldom/never- 40%, Don't know- 1%",
      "Frequency of meditation among Muslims": "Percent of Muslims who meditate: At least once a week- 35%, Once or twice a month- 8%, Several times a year- 7%, Seldom/never- 41%, Don't know- 8%",
      "Frequency of feeling spiritual peace and wellbeing among Muslims": "Percent of Muslims who feel a sense of spiritual peace and wellbeing: At least once a week- 64%, Once or twice a month- 13%, Several times a year- 10%, Seldom/never- 9%, Don't know- 4% ",
      "Frequency of feeling wonder about the universe among Muslims": "Percent of Muslims who feel a sense of wonder about the universe: At least once a week- 56%, Once or twice a month- 16%, Several times a year- 8%, Seldom/never- 17%, Don't know- 3%",
      "Sources of guidance on right and wrong among Muslims": "Percent of Muslims who say they look to…most for guidance on right and wrong: Religion- 47%, Philosophy/reason- 9%, Common sense- 36%, Science- 13%, Don't know- 4%",
      "Belief in absolute standards for right and wrong among Muslims": "Percent of Muslims who say: There are clear standards for what is right and wrong- 20%, Right or wrong depends on the situation- 76%, Neither/both equally- 1%, Don't know- 2%",
      "Frequency of reading scripture among Muslims": "Percent of Muslims who read scripture: At least once a week- 46%, Once or twice a month- 13%, Several times a year- 11%, Seldom/never- 28%, Don't know- 2%",
      "Interpreting scripture among Muslims": "Percent of Muslims who say the holy scripture is: Word of God; should be taken literally- 42%, Word of God; not everything taken literally- 31% Word of God; other/don't know- 10%, Not the word of God- 12%, Other/don't know- 5%",
      "Belief in Heaven among Muslims":"Percent of Muslims who…in heaven: Believe- 89%, Don't believe- 7%, Other/don't know- 4%",
      "Belief in Hell among Muslims": "Percent of Muslims who …in hell: Believe- 76%, Don't believe- 18%, Other/don't know- 6%",
      
      #Social And Political Views
      
      "Party affiliation among Muslims": "Percent of Muslims who identify as: Republicam/lean Rep.- 17%, No lean- 21%, Democrat/lean Dem.- 62%",
      "Political ideology among Muslims": "Percent of Muslims who are: Conservative- 22%, Moderate- 39%, Liberal- 33%, Don't know- 6%",
      "Views about size of government among Muslims": "Percent of Muslims who would rather have: Smaller government; fewer services- 23%, Bigger government; more services- 73%, Depends- 3%, Don't know- 2%",
      "Views about government aid to the poor among Muslims": "Percent of Muslims who say government aid to the poor: Does more harm than good- 30%, Does more good than harm- 63%, Neither/both equally- 4%, Don't know- 3%",
      "Views about abortion among Muslims": "Percent of Muslims who say abortion should be: Legal in all/most cases- 55%, Illegal in all/most cases- 37%, Don't know- 9%",
      "Views about homosexuality among Muslims": "Percent of Muslims who say homosexuality: Should be accepted- 45%, Should be discouraged- 47%, Neither/both equally- 5%, Don't know- 3%",
      "Views about same-sex marriage among Muslims": "Percent of Muslims who …same-sex marriage: Strongly favor/favor- 42%, Oppose/strongly oppose- 52%, Don't know- 6%",
      "Views about environmental regulation among Muslims": "Percent of Muslims who say: Stricter environmental laws and regulations cost too many jobs and hurt the economy- 27%, Stricter environmnetal laws and regulations are worth the cost- 67%, Neither/both equally- 3%, Don't know- 3%",
      "Views about human evolution among Muslims": "Percent of Muslims who say humans: Evolved; due to natural process- 25%, Evolved; due to God's design- 25%, Evolved; don't know how- 3%, Always exsited in present form- 41%, Don't know- 6%"

      #source: https://www.pewforum.org/religious-landscape-study/religious-tradition/muslim/
    }
    print(random.choice(list(dict.values())))

    
def Buddhist_Opinions():
    dict= {
      #Demographic Information

      "Age distribution among Buddhists": "Percent of Buddhists who are ages: 18-29- 34%, 30-49- 30%, 50-64- 23%, 65+ - 14%",
      "Generational cohort among Buddhists": "Percent of Buddhists who are: Younger Millenial- 23%, Older Millenial- 17%, Generation X- 23%, Baby Boomer- 30%, Silent- 7%, Greatest- <1%",
      "Gender composition among Buddhists":"Percent of Buddhists who are: Men- 51%, Women- 49%",
      "Racial and ethnic composition among Buddhists":"Percent of Buddhists who identify as: White- 44%, Black- 3%, Asian- 33%, LatinX- 12%, Other- 8%",
      "Immigrant status among Buddhists": "Percent of Buddhists who are: Immigrants- 26%, Second generation- 22%, Third generation or higher- 52%",
      "Income distribution among Buddhists": "Percent of Buddhists who have a household income of: Less than $30,000- 36%, $30,000-$49,999- 18%, $50,000-$99,999- 32%, $100,000 or more- 13%",
      "Educational distribution among Buddhists": "Percent of Buddhists who have completed: High school or less- 20%, Some college- 33%, College- 28%, Post-graduate degree- 20%",
      "Marital status among Buddhists": "Percent of Buddhists who are: Married- 39%, Living with a partner- 11%, Divorced/sparated- 10%, Widowed- 2%, Never married- 37%",
      "Parent of children under 18 among Buddhists": "Percent of Buddhists who are: Parents- 20%, Non-parents- 80%",
      
      #Beliefs And Practices

      "Belief in God among Buddhists": "Percent of Buddhists who say they: Believe in God; absolutely- 29%, Believe in God; fairly certain- 29%, Believe in God; not too/not at all certain- 10%, Believe in God; don't know- 1%, Do not believe in God- 27%, Other/don't know if they believe in God- 4%",
      "Importance of religion in one's life among Buddhists": "Percent of Buddhists who say religion is: Very important- 33%, Somewhat Important- 39%, Not too important- 15%, Not at all important- 10%, Don't know- 2%",
      "Attendance at religious services among Buddhists": "Percent of Buddhists who attend religious services: At least once a week- 18%, Once or twice a month/a few times a year- 50%, Seldom/never- 31%, Don't know- <1%",
      "Frequency of prayer among Buddhists": "Percent of Buddhists who pray: At least daily- 43%, Weekly- 16%, Monthly- 10%, Seldom/never- 29%, Don't know- 1%",
      "Frequency of participation in prayer, scripture study or religious education groups among Buddhists": "Percent of Buddhists who attend prayer group: At least once a week- 14%, Once or twice a month- 13%, Several times a year- 14%, Seldom/never- 58%, Don't know- 1%",
      "Frequency of meditation among Buddhists": "Percent of Buddhists who meditate: At least once a week- 66%, Once or twice a month- 6%, Several times a year- 7%, Seldom/never- 19%, Don't know- 1%",
      "Frequency of feeling spiritual peace and wellbeing among Buddhists": "Percent of Buddhists who feel a sense of spiritual peace and wellbeing: At least once a week- 59%, Once or twice a month- 14%, Several times a year- 14%, Seldom/never- 12%, Don't know- 1% ",
      "Frequency of feeling wonder about the universe among Buddhists": "Percent of Buddhists who feel a sense of wonder about the universe: At least once a week- 55%, Once or twice a month- 14%, Several times a year- 16%, Seldom/never- 15%, Don't know- 2%",
      "Sources of guidance on right and wrong among Buddhists": "Percent of Buddhists who say they look to…most for guidance on right and wrong: Religion- 8%, Philosophy/reason- 28%, Common sense- 44%, Science- 16%, Don't know- 5%",
      "Belief in absolute standards for right and wrong among Buddhists": "Percent of Buddhists who say: There are clear standards for what is right and wrong- 21%, Right or wrong depends on the situation- 75%, Neither/both equally- 4%, Don't know- <1%",
      "Frequency of reading scripture among Buddhists": "Percent of Buddhists who read scripture: At least once a week- 28%, Once or twice a month- 9%, Several times a year- 9%, Seldom/never- 53%, Don't know- 1%",
      "Interpreting scripture among Buddhists": "Percent of Buddhists who say the holy scripture is: Word of God; should be taken literally- 5%, Word of God; not everything taken literally- 9% Word of God; other/don't know- 1%, Not the word of God- 73%, Other/don't know- 12%",
      "Belief in Heaven among Buddhists":"Percent of Buddhists who…in heaven: Believe- 47%, Don't believe- 46%, Other/don't know- 7%",
      "Belief in Hell among Buddhists": "Percent of Buddhists who …in hell: Believe- 32%, Don't believe- 63%, Other/don't know- 5%",
      
      #Social And Political Views

      "Party affiliation among Buddhists": "Percent of Buddhists who identify as: Republicam/lean Rep.- 16%, No lean- 16%, Democrat/lean Dem.- 69%",
      "Political ideology among Buddhists": "Percent of Buddhists who are: Conservative- 16%, Moderate- 36%, Liberal- 44%, Don't know- 4%",
      "Views about size of government among Buddhists": "Percent of Buddhists who would rather have: Smaller government; fewer services- 40%, Bigger government; more services- 51%, Depends- 3%, Don't know- 6%",
      "Views about government aid to the poor among Buddhists": "Percent of Buddhists who say government aid to the poor: Does more harm than good- 22%, Does more good than harm- 73%, Neither/both equally- 4%, Don't know- 1%",
      "Views about abortion among Buddhists": "Percent of Buddhists who say abortion should be: Legal in all/most cases- 82%, Illegal in all/most cases- 17%, Don't know- 1%",
      "Views about homosexuality among Buddhists": "Percent of Buddhists who say homosexuality: Should be accepted- 88%, Should be discouraged- 10%, Neither/both equally- 1%, Don't know- 1%",
      "Views about same-sex marriage among Buddhists": "Percent of Buddhists who …same-sex marriage: Strongly favor/favor- 84%, Oppose/strongly oppose- 13%, Don't know- 3%",
      "Views about environmental regulation among Buddhists": "Percent of Buddhists who say: Stricter environmental laws and regulations cost too many jobs and hurt the economy- 20%, Stricter environmnetal laws and regulations are worth the cost- 77%, Neither/both equally- 1%, Don't know- 1%",
      "Views about human evolution among Buddhists": "Percent of Buddhists who say humans: Evolved; due to natural process- 67%, Evolved; due to God's design- 13%, Evolved; don't know how- 6%, Always exsited in present form- 13%, Don't know- 1%"

      #source: https://www.pewforum.org/religious-landscape-study/religious-tradition/buddhist/
    }
    print(random.choice(list(dict.values())))
    

    
def Nones_Opinions():
    dict= {
      #Demographic Information

      "Age distribution among 'nones'": "Percent of 'nones' who are ages: 18-29- 35%, 30-49- 37%, 50-64- 19%, 65+ - 9%",
      "Generational cohort among 'nones'": "Percent of 'nones' who are: Younger Millenial- 22%, Older Millenial- 22%, Generation X- 28%, Baby Boomer- 22%, Silent- 5%, Greatest- <1%",
      "Gender composition among 'nones'":"Percent of 'nones' who are: Men- 57%, Women- 43%",
      "Racial and ethnic composition among 'nones'":"Percent of 'nones' who identify as: White- 68%, Black- 9%, Asian- 5%, LatinX- 13%, Other- 4%",
      "Immigrant status among 'nones'": "Percent of 'nones' who are: Immigrants- 13%, Second generation- 12%, Third generation or higher- 75%",
      "Income distribution among 'nones'": "Percent of 'nones' who have a household income of: Less than $30,000- 33%, $30,000-$49,999- 20%, $50,000-$99,999- 26%, $100,000 or more- 21%",
      "Educational distribution among 'nones'": "Percent of 'nones' who have completed: High school or less- 38%, Some college- 32%, College- 18%, Post-graduate degree- 11%",
      "Marital status among 'nones'": "Percent of 'nones' who are: Married- 37%, Living with a partner- 11%, Divorced/sparated- 11%, Widowed- 3%, Never married- 37%",
      "Parent of children under 18 among 'nones'": "Percent of 'nones' who are: Parents- 26%, Non-parents- 74%",
      
      #Beliefs And Practices

      "Belief in God among 'nones'": "Percent of 'nones' who say they: Believe in God; absolutely- 27%, Believe in God; fairly certain- 22%, Believe in God; not too/not at all certain- 11%, Believe in God; don't know- 1%, Do not believe in God- 33%, Other/don't know if they believe in God- 6%",
      "Importance of religion in one's life among 'nones'": "Percent of 'nones' who say religion is: Very important- 13%, Somewhat Important- 21%, Not too important- 26%, Not at all important- 39%, Don't know- 1%",
      "Attendance at religious services among 'nones'": "Percent of 'nones' who attend religious services: At least once a week- 4%, Once or twice a month/a few times a year- 24%, Seldom/never- 72%, Don't know- <1%",
      "Frequency of prayer among 'nones'": "Percent of 'nones' who pray: At least daily- 20%, Weekly- 11%, Monthly- 7%, Seldom/never- 62%, Don't know- 1%",
      "Frequency of participation in prayer, scripture study or religious education groups among 'nones'": "Percent of 'nones' who attend prayer group: At least once a week- 5%, Once or twice a month- 3%, Several times a year- 4%, Seldom/never- 88%, Don't know- <1%",
      "Frequency of meditation among 'nones'": "Percent of 'nones' who meditate: At least once a week- 26%, Once or twice a month- 10%, Several times a year- 5%, Seldom/never- 58%, Don't know- 1%",
      "Frequency of feeling spiritual peace and wellbeing among 'nones'": "Percent of 'nones' who feel a sense of spiritual peace and wellbeing: At least once a week- 40%, Once or twice a month- 16%, Several times a year- 11%, Seldom/never- 32%, Don't know- 2% ",
      "Frequency of feeling wonder about the universe among 'nones'": "Percent of 'nones' who feel a sense of wonder about the universe: At least once a week- 47%, Once or twice a month- 16%, Several times a year- 12%, Seldom/never- 24%, Don't know- 2%",
      "Sources of guidance on right and wrong among 'nones'": "Percent of 'nones' who say they look to…most for guidance on right and wrong: Religion- 7%, Philosophy/reason- 18%, Common sense- 57%, Science- 17%, Don't know- 2%",
      "Belief in absolute standards for right and wrong among 'nones'": "Percent of 'nones' who say: There are clear standards for what is right and wrong- 20%, Right or wrong depends on the situation- 78%, Neither/both equally- 1%, Don't know- 1%",
      "Frequency of reading scripture among 'nones'": "Percent of 'nones' who read scripture: At least once a week- 9%, Once or twice a month- 6%, Several times a year- 6%, Seldom/never- 79%, Don't know- <1%",
      "Interpreting scripture among 'nones'": "Percent of 'nones' who say the holy scripture is: Word of God; should be taken literally- 10%, Word of God; not everything taken literally- 11% Word of God; other/don't know- 1%, Not the word of God- 72%, Other/don't know- 7%",
      "Belief in Heaven among 'nones'":"Percent of 'nones' who…in heaven: Believe- 27%, Don't believe- 53%, Other/don't know- 9%",
      "Belief in Hell among 'nones'": "Percent of 'nones' who …in hell: Believe- 27%, Don't believe- 65%, Other/don't know- 8%",
      
      #Social And Political Views

      "Party affiliation among 'nones'": "Percent of 'nones' who identify as: Republicam/lean Rep.- 23%, No lean- 22%, Democrat/lean Dem.- 54%",
      "Political ideology among 'nones'": "Percent of 'nones' who are: Conservative- 18%, Moderate- 36%, Liberal- 39%, Don't know- 8%",
      "Views about size of government among 'nones'": "Percent of 'nones' who would rather have: Smaller government; fewer services- 47%, Bigger government; more services- 46%, Depends- 3%, Don't know- 4%",
      "Views about government aid to the poor among 'nones'": "Percent of 'nones' who say government aid to the poor: Does more harm than good- 36%, Does more good than harm- 58%, Neither/both equally- 4%, Don't know- 2%",
      "Views about abortion among 'nones'": "Percent of 'nones' who say abortion should be: Legal in all/most cases- 73%, Illegal in all/most cases- 23%, Don't know- 4%",
      "Views about homosexuality among 'nones'": "Percent of 'nones' who say homosexuality: Should be accepted- 83%, Should be discouraged- 12%, Neither/both equally- 3%, Don't know- 3%",
      "Views about same-sex marriage among 'nones'": "Percent of 'nones' who …same-sex marriage: Strongly favor/favor- 78%, Oppose/strongly oppose- 16%, Don't know- 6%",
      "Views about environmental regulation among 'nones'": "Percent of 'nones' who say: Stricter environmental laws and regulations cost too many jobs and hurt the economy- 27%, Stricter environmnetal laws and regulations are worth the cost- 68%, Neither/both equally- 2%, Don't know- 3%",
      "Views about human evolution among 'nones'": "Percent of 'nones' who say humans: Evolved; due to natural process- 63%, Evolved; due to God's design- 14%, Evolved; don't know how- 4%, Always exsited in present form- 15%, Don't know- 3%"

      #source: https://www.pewforum.org/religious-landscape-study/religious-tradition/unaffiliated-religious-nones/
    }
    print(random.choice(list(dict.values())))
    


def Christianity_Fun_Facts():

  fun_facts=["Followers of the Christian religion base their beliefs on the life, teachings and death of Jesus Christ.",
             "Christians believe in one God that created heaven, earth and the universe. The belief in one God originated with the Jewish religion.",
            "Christians believe Jesus is the 'Messiah' or savior of the world. They also believe that he is the son of God.",
            "Jesus was born in a manger in Bethlehem to Mary, a virgin at the time of conception, and Joseph, her husband. Mary was visited by the angel Gabriel and told she would conceive a son, though she was not yet married and a virgin and he would be the Messiah.",
            "Jesus was crucified on a cross. His death made salvation and forgiveness of sins possible for all.",
            "On the third day after his crucifixion, Jesus arose from the dead. His resurrection is celebrated on Easter, which is considered Christianity's most important holiday",
            "After Jesus' crucifixion and resurrection, God's presence remained on earth in the form of the Holy Spirit to be a comforter to all.",
            "Salvation can only be obtained by believing that Jesus was sent by God to forgive the sins of every human, and to confess those sins to him.",
            "Interpretations of the Bible and the practices of each church vary by denomination, but the belief in one God and Jesus as the Messiah is central to all Christians.",
            "The first Christians were Jews who came to believe Jesus was the Messiah. Gentiles (non-Jews) also made up a large majority of its followers, as is the case today.",]

  
  print (random.choice(fun_facts))

  # source: https://www.cnn.com/2013/11/12/world/christianity-fast-facts/index.html
 

def Judaism_Fun_Facts():
    
  fun_facts= ["Jewish law is rooted in the Torah, the first five books of the Bible: Genesis, Exodus, Leviticus, Numbers and Deuteronomy.",
      "According to the Torah, Abraham is the father of Judaism. He was born about 4,000 years ago, during an era when many gods were worshiped, but he believed there was only one God.",
      "Judaism grew out of a covenant between God, Abraham, Abraham's children and their descendants. Moses, likely born during the late 14th century BC, led the Hebrew slaves out of Egypt, received the Torah from God and taught the people God's laws.",
      "The main denominations of Judaism are Orthodox, Conservative and Reform.",
      "Jewish people worship at synagogues, and any educated member of the congregation can lead a service. However, a rabbi or cantor usually leads services.",
      "Rabbis are Jewish spiritual authorities, educated at yeshivas, religious seminaries. Rabbis interpret the Bible and present the meaning of Jewish law.",
      "When Jewish children turn 12 or 13, they stand before the congregation and read a section of the Torah in a ceremony called a bar mitzvah (for boys) or bat mitzvah (for girls). This celebration commemorates a passage into Jewish adulthood, meaning that the young men and women can now participate fully in traditions like fasting on Yom Kippur.",
      "Observant Jews keep kosher, following dietary laws that prohibit the eating of certain foods including shellfish and pork, as well as meals that contain a mix of meat and dairy.",
      "A yarmulke or kippa is a cap worn by Jewish men as well as secular men at religious ceremonies. The custom isn't rooted in the Bible but evolved out of the belief that God is watching from above.",
      "Shabbat, the Sabbath or day of rest, begins Friday night and lasts until sundown Saturday.",
      "Rosh Hashanah, the Jewish New Year, and Yom Kippur, the Day of Atonement, are the holiest days of the year, known as the High Holy Days.",
      "Passover, also called Pesach, marks the exodus of the Israelites from Egyptian slavery.",
      "Judaism was established circa 2000 BC as part of a covenant between God and Abraham. Uprisings against the Romans during the first and second centuries AD led to the beginning of the Jewish diaspora, the movement of Jews into other parts of the world. Those practicing Judaism were kept marginalized from society and persecuted in many countries. The creation of a Jewish state was discussed at the first Zionist Congress in Switzerland in 1897. In 1948, the state of Israel was formed, after World War II and the genocide of over six million Jews."]

  print (random.choice(fun_facts))

  # source: https://www.cnn.com/2013/11/12/world/judaism-fast-facts/index.html
    
def Hinduism_Fun_Facts():
  
  fun_facts= ["79.8% of India's population is Hindu. As of 2015, approximately 15.1% of the world population is Hindu. 79.8% of India's population is Hindu. 0.7% of American adults practice Hinduism.",
      "There is no single founder or founding incident of Hinduism. It grew out of cultural and religious changes in India.",
      "The Hindu belief is that gods or divinities can take many forms, but all form one universal spirit called Brahman. The three most important representations of Brahman are Brahma, the creator of the universe, Vishnu, the preserver of the universe, and Shiva, the destroyer of the universe.",
      "The Hindu belief involves reincarnation of the soul, which is rebirth after death. Hindus believe the conditions of one's present life are due to karma or accumulated good or bad behavior in past lives.",
      "One improves one's conditions through good behavior and creates suffering for oneself through bad behavior. Eventually the soul will achieve moksha, or salvation, and stop the cycle of rebirths to become a part of the absolute soul.",
      "Paths to salvation are called the margas or yogas. karma marga - performing social obligations and offering selfless service.  jnana marga - studying and cultivating an intellectual understanding into one's identity with Brahman. bhakti marga - devotion to one's personal god. raja or dhyana marga - not as widely recognized as the three outlined in the Bhagavad Gita, this path uses meditation to gain insight into the absolute soul that resides within one's self.",
      "There are multiple sects, theologies, and beliefs in Hinduism, and there is no single book of doctrine. It is an inclusive religious group, allowing for a lot of diversity.",
      "The Vedas are the primary literary works, containing sacred verses and hymns composed in Sanskrit. The Rig Veda was the first of the four Vedas. The Samaveda, Yajurveda and Atharvaveda followed later.",
      "Pilgrimages and festivals are common in Hinduism. Diwali, the New Year's celebration, features giving of gifts and lighting of ceremonial lamps. Holi, the Festival of Colors, marks the arrival of spring each year.",
      "Indian society has traditionally been divided into a hierarchical system called caste or jati, which is not limited to Hindus, but which most Hindus have observed throughout history. It is hereditary and each caste has its own set of values, rules, dietary beliefs, etc. Many do not marry outside their castes. Although Hinduism teaches that discrimination and prejudice go against the idea of the divinity of all beings, both sometimes exist within the caste system.",
      "Mahatma Gandhi called these untouchables (lowest in cast system) 'children of God.' Although the 1950 Indian constitution outlawed 'untouchability,' violence against them continues.",
      "Mahatma Gandhi was shot and killed by a Hindu fanatic who disagreed with his efforts to reconcile Hindus and Muslims on January 30, 1948. Gandhi, born October 2, 1869, is considered the father of modern India. He was raised in a highly religious family and practiced law. He led a campaign of non-violent protests against British rule, which eventually led to India's independence in 1947."]

  print (random.choice(fun_facts))
  
# source: https://www.cnn.com/2013/11/07/world/hinduism-fast-facts/index.html


def Mormon_Fun_Facts():
  
  fun_facts= ["Joseph Smith Jr. (December 23, 1805-June 27, 1844) founded the Church of Jesus Christ of Latter-Day Saints around 1830. He is seen as a living prophet.",
      "'The Book of Mormon' is believed to be the result of Joseph Smith's communion with the divine. It is also the source of the common nickname for the church and its followers, Mormons (formally known as Church of Jesus Christ of Latter-day Saints).",
      "Joseph Smith claimed to have begun receiving messages at age 14 from God, Jesus Christ and other heavenly messengers.",
      "Mormons consider themselves to be Christians. They follow the teachings found within the Christian 'Bible,' 'The Book of Mormon,' 'Doctrine and Covenants' and 'Pearl of Great Price.'",
      "'The Book of Mormon' tells the story of Israelites who left Jerusalem around 600 BC and traveled to North America after a calling from God. They set up civilizations, and centuries later witnessed an appearance by Jesus Christ after his crucifixion and resurrection.",
      "They believe that God sent many prophets to spread his word after Jesus Christ's death and resurrection.",
      "The church is led by a prophet who also serves as president of the church. The president serves for life.",
      "The church's organizational hierarchy is the all-male General Authorities: the First Presidency (the president and two counselors), the Quorum of the Twelve Apostles, the First Quorum of the Seventy, the Second Quorum of the Seventy and the Presiding Bishopric (the bishop and two counselors); and the General Auxiliaries: the Primary, the all-female Relief Society, Sunday School, Young Men and Young Women.",
      "Children are baptized at age eight. New members are also baptized.",
      "There are two orders of priesthood. A young man 12 or older can enter into the Aaronic priesthood, seen as an earthly priesthood. Melchizedek priesthood can be obtained when a man turns 18. This entails spiritual and heavenly duties.",
      "They follow a strict health code that prohibits the consumption of tobacco, alcohol, tea and coffee.",
      "They are encouraged to tithe - giving 10% of their earnings to the church.",
      "Many church members, between the ages 18 and 25 for males and 19 and 25 for females, become missionaries. Single men serve for two years; single women for 18 months.",
      "The church is headquartered in Salt Lake City, Utah, USA."]
  
  print (random.choice(fun_facts))

  #source: https://www.cnn.com/2013/11/12/us/mormon-church-fast-facts/index.html

    
def Islam_Fun_Facts():
  
  fun_facts= ["The word Islam translates as 'submission' or 'surrender.' Surrender to the will of Allah - Arabic for God.",
      "Islam is partially based on the Judeo-Christian religions. It has a monotheistic (belief in one God) message, and follows some of the same principles as Christianity and Judaism.",
      "The followers of Islam, Muslims, believe in one God, Allah, and believe Muhammad was his prophet. They also believe Adam, of the Bible's Old Testament, was the first prophet. Other prophets include Abraham, Moses, Noah, David and Jesus.",
      "There are five 'Pillars of Islam' that Muslims follow: The Shahadah - A statement of faith all Muslims recite at least one time in their lives,  The Salat or Salah - A daily ritual prayer of faith done five times a day,  Zakat - a tax paid to benefit the poor or those in need,  Sawm - a fast done during the month of Ramadan,  Hajj - a pilgrimage every Muslim must do at least once in his/her life, if he or she can afford it, to the Holy city of Mecca, in modern-day Saudi Arabia. The pilgrimage begins on the seventh or eighth day of the last month of the Islamic lunar calendar, and ends on the 12th day of that same month. The Kaaba is the shrine located in Mecca, which is visited during the pilgrimage (or Hajj). It is the most holy place for Muslims.",
      "Two other main holy places (besides The Kabba in Mecca, which is the most holy) are the Prophet Muhammad's mosque in the city of Medina in Saudi Arabia, and 'Al-Aqsa' mosque in Jerusalem.",
      "Muslims believe the Quran is the divine words or revelations on which they base their faith. Muslims believe the Angel Gabriel delivered the ideas in the Quran to Muhammad.",
      "The Hadith is a collection of the traditions and sayings of Muhammad, also used to frame the Muslim way of life and beliefs.",
      "According to Islamic traditions, Jihad is the struggle exerted while following God's commands at both a personal level as well as at a community level.",
      "Sunni is the largest branch of Islam. They accept that the first four caliphs (leaders) are the legitimate successors to Muhammad.",
      "Shiite, or Shia, the second-largest branch of Islam, believes only the caliph Ali and his descendants are the legitimate successors to Muhammad and reject the first three caliphs.",
      "Kharijites are members of the earliest sect in Islam that left the followers of Ali; their break with the Shiite was over the selection method for a new leader. They were known for uncompromising positions on the observance of the Quran and for radical fundamentalism. Today they are known as the Ibadi or Ibadities.",
      "The Nation of Islam is a primarily African-American Sunni sect, founded in the 1930s in Detroit, Michigan.",
      "Sharia is an Arabic word originally meaning 'the path leading to the source of water'. It is derived from the Quran and the life of the Prophet Muhammad and his followers. It is a system of morals, religious observance, ethics, and politics that covers both religious and non-religious aspects of life. Many Muslim countries use Sharia law as a basis for their laws. It differs from Western legal systems in that the scope of Sharia law is much larger and the Islamic concept of law results from the expression of the divine will.",
      "According to a report by the Pew Research Center, there are 1.8 billion Muslims worldwide. (2015 est.)",
      "Islam is the second-largest religion in the world, following Christianity."]

  print (random.choice(fun_facts))

  # source: https://www.cnn.com/2013/11/12/world/islam-fast-facts/index.html


def Buddhism_Fun_Facts():
 
  fun_facts=["Buddhism is the major religion in many countries in Asia",
      "Siddhartha Gautama (Buddha) grew up in a wealthy family. He decided to follow a path of self-denial, but did not find truth until he sat down under a tree, now known as the Bo tree. There he was 'enlightened' and obtained the knowledge he had been looking for. According to legend, Buddha sat under the Bo tree for 49 days and was tempted by demons. He discovered four noble truths and the Eightfold Path to Nirvana, or ultimate bliss.",
      "The Four Noble Truths of Buddhism: 1) existence is suffering, 2) the cause of suffering is craving and attachment, 3) suffering ceases at some point and turns to Nirvana (liberation or total bliss) and 4) there is a path to Nirvana which is made up of eight steps, sometimes called the Eightfold Path. The Eightfold Path to Nirvana is to be 'right' in all these areas: concentration, views, speech, resolve, action, livelihood, effort, and mindfulness.",
      "There are two major schools of Buddhism: Mahayana and Theravada or Hinayana. There is a third school, the Vajrayana, but it only has a small following. Dozens of different sects of Buddhism are derived from these schools, all having different characteristics, but sharing the basic beliefs.",
      "Buddhists believe in reincarnation and that one must stop the cycle of rebirth as a suffering, selfish individual, and must attain Nirvana, which is the highest point and the end of the self.",
      "Karma is the belief that good deeds/behavior will be visited back on individuals as well as bad deeds/behavior. This is the basis for living a good, moral life.",
      "The Pali Tipitaka is the earliest collection of sacred Buddhist writings; used mostly in the Theravada school. Translated, it means the 'Three Baskets.'",
      "According to Pew Research Center, there are approximately 488 million Buddhists worldwide.",
      "One in seven Asian Americans, or 14%, are Buddhist. About 1% of the general public in the United States is Buddhist, according to Pew.",
      "There is no belief in a personal God. Buddhism is not centred on the relationship between humanity and God",
      "Buddhists believe that nothing is fixed or permanent - change is always possible",
      "The path to Enlightenment is through the practice and development of morality, meditation and wisdom."]

  
  print (random.choice(fun_facts))

  # sources: https://www.cnn.com/2013/11/11/world/buddhism-fast-facts/index.html
           #  https://www.bbc.co.uk/religion/religions/buddhism/ataglance/glance.shtml
        
        
def Nones_Fun_Facts():
  
  fun_facts= ["22.8% of Americans identiy as a 'none'",
      "37% of Vermont identifies as a 'none', the most out of any state",
      "12% of Alaba,a identifies as a 'none', the least out of any state",
      "According to Pew Research Center,'nones' identify as unafiliated, separate from athiest and agnostic",
      "Spiritual but not religious is a popular identity among the 'nones'",
      "Many 'nones' believe in a god but dislike organized religion",
      "Nones are more conentrated in the Western US than any other region",
      "More than half of the nones (52 percent) say religious institutions protect and strengthen morality, though an even greater proportion (70 percent) believes these institutions are too concerned with money and power.",
      "'Nones' are more heavily concentrated among men than women. But the growth of the unaffiliated has not been limited to certain demographic categories; a rise in the share of unaffiliated has been seen across a variety of racial and ethnic groups, among people with different levels of education and income, among immigrants and the native born, and throughout all major regions of the country.",
      "Only about 9% of U.S. adults say they were raised without a religious affiliation, and among this group, roughly half say that they now identify with a religion (most often Christianity). But nearly one-in-five Americans (18%) have moved in the other direction, saying that they were raised as Christians or members of another faith but that they now have no religious affiliation.",
      "Nones” are more heavily concentrated among men than women. But the growth of the unaffiliated has not been limited to certain demographic categories; a rise in the share of unaffiliated has been seen across a variety of racial and ethnic groups, among people with different levels of education and income, among immigrants and the native born, and throughout all major regions of the country.",
      "Many are looking for spiritual community – just not necessarily a religious community."]

  print (random.choice(fun_facts))

  #source: https://factsandtrends.net/2014/11/17/10-facts-about-nones-in-the-u-s/
          # https://www.pewresearch.org/fact-tank/2015/05/13/a-closer-look-at-americas-rapidly-growing-religious-nones/
    
    
def Christian_Info():
  user_input= input("Would you like a fun fact about Christianity or to learn about Christian opinions in the United States? \
  Please enter an option: [Fun fact][Opinion]")
    
  if (user_input.lower()== "fun fact"):
        Christianity_Fun_Facts()
        print("")

  elif (user_input.lower()== "opinion"):
          Christian_Opinions()
          print("")


def Hinduism_Info():
  user_input= input("Would you like a fun fact about Hinduism or to learn about Hindi opinions in the United States? \
  Please enter an option: [Fun fact][Opinion]")

  if (user_input.lower()== "fun fact"):
        Hinduism_Fun_Facts()
        print("")
  elif (user_input.lower()== "opinion"):
          Hindu_Opinions()
          print("")
            
            
def Unafilliated_Info():
  user_input= input("Would you like a fun fact about those that identify as Unafilliated or to learn about Unafilliated opinions in the United States? \
  Please enter an option: [Fun fact][Opinion]")

  if (user_input.lower()== "fun fact"):
        
        Nones_Fun_Facts()
        print("")

  elif (user_input.lower()== "opinion"):
          Nones_Opinions()
          print("")
            

def Jewish_Info():
  user_input= input("Would you like a fun fact about Judaism or to learn about Jewish opinions in the United States? \
  Please enter an option: [Fun fact][Opinion]")

  if (user_input.lower()== "fun fact"):
        Judaism_Fun_Facts()
        print("")

  elif (user_input.lower()== "opinion"):
          Jewish_Opinions()
          print("")
            
            
def Mormon_Info():
  user_input=input("Would you like a fun fact about Mormon beliefs or to learn about Mormon opinions in the United States? \
  Please enter an option: [Fun fact][Opinion]")

  if (user_input.lower()== "fun fact"):
        Mormon_Fun_Facts()
        print("")

  elif (user_input.lower()== "opinion"):
          Mormon_Opinions()
          print("")
            
def Islam_Info():
  user_input= input("Would you like a fun fact about Muslim beliefs or to learn about Muslim opinions in the United States? \
  Please enter an option: [Fun fact][Opinion]")

  if (user_input.lower()== "fun fact"):
        Islam_Fun_Facts()
        print("")

  elif (user_input.lower()== "opinion"):
          Muslim_Opinions()
          print("")
            
def Buddhist_Info():
  user_input= input("Would you like a fun fact about Buddhism or to learn about Buddhist opinions in the United States? \
  Please enter an option: [Fun fact][Opinion]")

  if (user_input.lower()== "fun fact"):
        Buddhism_Fun_Facts()
        print("")

  elif (user.input.lower()== "opinion"):
          Buddhist_Opinions()
          print("")
            
            
choice=""
while choice != "Q":
  user_input= input("What religion would you like to learn about? Choose one of the options below: \
  [Christianity][Judaism][Unafilliated][Hinduism][Mormons][Buddhism]")

  user_input.strip()

  if user_input== "Christianity":
    Christian_Info()
    

  elif user_input== "Judaism":
    Jewish_Info()
      

  elif user_input== "Unafilliated":
    Unafilliated_Info()

  elif user_input== "Hinduism":
    Hindu_Info()

  elif user_input== "Mormons":
    Mormon_Info()

  elif user_input== "Buddhism":
    Buddhist_Info()
    print("bye")
    
  elif user_input== "Islam":
    Islam_Info()
    
  elif user_input== "Q":
    choice= "Q"
  
  else:
    print("Sorry, this is not an option. Please enter a valid option or enter Q to quit")

  print("Enter Q to quit")
