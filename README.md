# MU Hiring 2022 Dataset
My team and I got some fuzzfied data sets that we defuzzified and then analysed the data and put our conclusion on a website built with the help of streamlit. 

After looking at the data analysis we came up with a business model to be a consulting/analysis company for the organiser which works on SAAS bases

To check the website just clone the repo ,check if you have all the libraries mentioned in requirements.txt and then-: 
    streamlit run app.py 
  
 That should lead you to the website

**TL;DR**
1. Prepare unified student profiles from the activity data provided
    <br>a. Will be validated aganist masked source data
2. Pitch a business solution using analysis of the profiles built
    <br>a. Judged by a panel
## General information
- Number of clubs: 3
- Number of fests: 2
## Dataset description
- College provided source truth: [Metadata](Metadata.csv)
- All club events data: [Clubs_data](Clubs_data.csv)
- All Organizers for fests: [Organisers_In_Fests](Organisers_In_Fests.csv)
- Participation list from all fest related events: [Participants_In_Fests](Participants_In_Fests.csv)

## Mandatory tech features
1. Streamlit
2. Profile JSON should be submitted before presentation
3. Pluggable format



## Sample Profile json format
```
{
        "Name": "annette ahmed",
        "Id": "18XJ1A0100",
        "Clubs": {
            "club_1": {
                "isOrganiser": "organiser_1",
                "club_1_event_3": {
                    "Participated": false
                }
            },
            "club_3": {
                "isOrganiser": "",
                "club_3_event_1": {
                    "Participated": true
                }
            },
            "club_2": {
                "isOrganiser": "",
                "club_2_event_2": {
                    "Participated": true
                }
            }
        },
        "Fests": {
            "fest_2": {
                "isOrganiser": "organiser_9",
                "fest_2_event_5": {
                    "Participated": true
                }
            },
            "fest_1": {
                "isOrganiser": "organiser_9",
                "fest_1_event_5": {
                    "Participated": true
                }
            }
        }
    }

```
