import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Loading the Saved Models

diabetes_model=pickle.load(open("saved_models/diabetes_model.sav", 'rb'))

heart_disease_model=pickle.load(open("saved_models/heart_disease_model.sav",'rb'))

parkinsons_model=pickle.load(open("saved_models/parkinsons_model.sav", 'rb'))

breast_cancer_model=pickle.load(open("saved_models/breast_cancer_model.sav", 'rb'))



# Sidebar For Navigation
with st.sidebar:
    
    selected=option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Breast Cancer Prediction'],
                          icons=['activity','heart','person','circle'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected=='Diabetes Prediction'):
    
    # Page Title
    st.title('Diabetes Prediction using ML')
    
    
    # Getting the Input Data from the User
    col1, col2, col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose=st.text_input('Glucose Level')
    
    with col3:
        BloodPressure=st.text_input('Blood Pressure Value')
    
    with col1:
        SkinThickness=st.text_input('Skin Thickness Value')
    
    with col2:
        Insulin=st.text_input('Insulin Level')
    
    with col3:
        BMI=(st.text_input('BMI Value'))
    
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age=st.text_input('Age of the Person')
    
    
    # Code for Prediction
    diab_diagnosis=''
    
    # Creating a Button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0]==1):
          diab_diagnosis="The Person is Diabetic😢"
        else:
          diab_diagnosis="The Person is Not Diabetic😊"
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected=='Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3=st.columns(3)
    
    with col1:
        age=st.text_input('Age')
        
    with col2:
        sex=st.text_input('Sex')
        
    with col3:
        cp=st.text_input('Chest Pain Types')
        
    with col1:
        trestbps=st.text_input('Resting Blood Pressure')
        
    with col2:
        chol=st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs=st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg=st.text_input('Resting Electrocardiographic Results')
        
    with col2:
        thalach=st.text_input('Maximum Heart Rate Achieved')
        
    with col3:
        exang=st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak=st.text_input('ST Depression Induced by Exercise')
        
    with col2:
        slope=st.text_input('Slope of the Peak Exercise ST Segment')
        
    with col3:
        ca=st.text_input('Major Vessels Colored by Flourosopy')
        
    with col1:
        thal=st.text_input('Thal: 0 = Normal; 1 = Fixed Defect; 2 = Reversable Defect')
        
        
     
     
    # Code for Prediction
    heart_diagnosis=''
    
    # Creating a Button For Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0]==1):
          heart_diagnosis="The Person is Having Heart Disease😢"
        else:
          heart_diagnosis="The Person does not Have Any Heart Disease😊"
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected=="Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5=st.columns(5)  
    
    with col1:
        fo=st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi=st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo=st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent=st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP=st.text_input('MDVP:RAP')
        
    with col2:
        PPQ=st.text_input('MDVP:PPQ')
        
    with col3:
        DDP=st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer=st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB=st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3=st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5=st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ=st.text_input('MDVP:APQ')
        
    with col4:
        DDA=st.text_input('Shimmer:DDA')
        
    with col5:
        NHR=st.text_input('NHR')
        
    with col1:
        HNR=st.text_input('HNR')
        
    with col2:
        RPDE=st.text_input('RPDE')
        
    with col3:
        DFA=st.text_input('DFA')
        
    with col4:
        spread1=st.text_input('spread1')
        
    with col5:
        spread2=st.text_input('spread2')
        
    with col1:
        D2=st.text_input('D2')
        
    with col2:
        PPE=st.text_input('PPE')
        
    
    
    # Code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction=parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis="The Person has Parkinson's Disease😢"
        else:
          parkinsons_diagnosis="The Person does not Have Parkinson's Disease😊"
        
    st.success(parkinsons_diagnosis)




    # Breast Cancer Prediction Page
if (selected=="Breast Cancer Prediction"):
    
    # page title
    st.title("Breast Cancer Prediction using ML")
    
    col1, col2, col3, col4, col5=st.columns(5)  
    
    with col1:
        mr=st.text_input('Mean Radius')
        
    with col2:
        mt=st.text_input('Mean Texture')
        
    with col3:
        mp=st.text_input('Mean Perimeter')
        
    with col4:
        ma=st.text_input('Mean Area')
        
    with col5:
        ms=st.text_input('Mean Smoothness')
        
    with col1:
        mcs=st.text_input('Mean Compactness')
        
    with col2:
        mcy=st.text_input('Mean Concavity')
        
    with col3:
        mcp=st.text_input('Mean Concave Points')
        
    with col4:
        msy=st.text_input('Mean Symmetry')
        
    with col5:
        mfd=st.text_input('Mean Fractal Dimension')
        
    with col1:
        re=st.text_input('Radius Error')
        
    with col2:
        te=st.text_input('Texture Error')
        
    with col3:
        pe=st.text_input('Perimeter Error')
        
    with col4:
        ae=st.text_input('Area Error')
        
    with col5:
        se=st.text_input('Smoothness Error')
        
    with col1:
        ce=st.text_input('Compactness Error')
        
    with col2:
        cye=st.text_input('Concavity Error')
        
    with col3:
        cpe=st.text_input('Concave Points Error')
        
    with col4:
        sye=st.text_input('Symmetry Error')
        
    with col5:
        fde=st.text_input('Fractal Dimension Error')
        
    with col1:
        wr=st.text_input('Worst Radius')
        
    with col2:
        wt=st.text_input('Worst Texture')
    
    with col3:
        wp=st.text_input('Worst Perimeter')
        
    with col4:
        wa=st.text_input('Worst Area')
        
    with col5:
        ws=st.text_input('Worst Smoothness')

    with col1:
        wc=st.text_input('Worst Compactness')
        
    with col2:
        wcy=st.text_input('Worst Concavity')
        
    with col3:
        wcp=st.text_input('Worst Concave Points')
        
    with col4:
        wsy=st.text_input('Worst Symmetry')
        
    with col5:
        wfd=st.text_input('Worst Fractal Dimension')

    
        
    # Code for Prediction
    breast_diagnosis = ''
    
    # Creating a Button for Prediction    
    if st.button("Breast Cancer Test Result"):
        input_data=[[float(mr), float(mt), float(mp), float(ma), float(ms), float(mcs), float(mcy), float(mcp), float(msy), float(mfd), float(re), float(te), float(pe), float(ae), float(se), float(ce), float(cye), float(cpe), float(sye), float(fde), float(wr), float(wt), float(wp), float(wa), float(ws), float(wc), float(wcy), float(wcp), float(wsy), float(wfd)]]
        #breast_cancer_prediction=breast_cancer_model.predict([[mr, mt, mp, ma, ms, mcs, mcy, mcp, msy, mfd, re, te, pe, ae, se, ce, cye, cpe, sye, fde, wr, wt, wp, wa, ws, wc, wcy, wcp, wsy, wfd]])                          
        breast_cancer_prediction=breast_cancer_model.predict(input_data)
        if (breast_cancer_prediction[0] == 1):
          breast_diagnosis="The Person has Breast Cancer😢"
        else:
          breast_diagnosis="The Person does not Have Breast Cancer😊"
        
    st.success(breast_diagnosis)


