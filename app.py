# import streamlit packages

import streamlit as st 


#calculate BMR (basal metabolic rate)
def bmr_calculate(gender, weight, height, age):
    if gender == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr


def daily_caloric(bmr,activity_level):
    activity_fac = {
        "Sedentary": 1.2,
        "Lightly active": 1.375,
        "Moderately active": 1.55,
        "Very active": 1.725,
        "Super active": 1.9
    }
    
    return bmr * activity_fac[activity_level]



#streamlit part  
def main():   
  st.title("Track, Predict, and Understand the Health Implications of Your Weight Journey")
  st.markdown("🏋️  💪  🏋️‍♂️")
  st.title("Weight lose and Weight gain :- ")
  st.markdown("---")
  gender = st.selectbox("gender",[" male","female"])
  age = st.slider(label="select your age", min_value = 10, max_value = 80,value = 25,step = 1)
  weight = st.slider(label= "Select your Weight in (KG)",min_value = 30,max_value = 300,value = 65,step = 1)
  height = st.slider(label= "Select your Height in (cm)",min_value = 120,max_value = 200,value = 165,step = 1)
  goal_weight = st.number_input(label="Select your weight goal (kg)", min_value=30, max_value=200, value=65, step=1)
  activity_level = st.selectbox("Acticity Level",["Sedentary", "Lightly active", "Moderately active", "Very active", "Super active"])
  goal_type = "gain" if goal_weight > weight else "lose"




# set a button
  if st.button("Calculate"):
      bmr = bmr_calculate(gender, weight, height, age)
      daily_caloric_need =  daily_caloric(bmr,activity_level)  
      
      
      st.write(f" You Basal Metbolic Rate (BMR) is : {bmr:2f} caloric/day  ")
      st.write(f"You daily caloric need based on activity:{daily_caloric_need:2f} caloric/day")
      
      calorie_deficit_surplus=500
      
  if goal_type == "lose":
       daily_caloric_intake = daily_caloric_need - calorie_deficit_surplus
       weeks_needed = ((weight - goal_weight) * 7700) / (calorie_deficit_surplus * 7)
  else:
       daily_caloric_intake = daily_caloric_need + calorie_deficit_surplus
       weeks_needed = ((goal_weight - weight) * 7700) / (calorie_deficit_surplus * 7)
              
              
  st.write(f"To {goal_type} weight, you need to consume approximately {daily_caloric_intake:.2f} calories/day.")
  st.write(f"Estimated time to reach your goal weight: {weeks_needed:.2f} weeks.")
        
if __name__ == "__main__":
    main()



    

  