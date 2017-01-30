# -*- coding: utf-8 -*-
#Desired APP URL
CureatrPlayURL="https://cureatr-vm.dev:5101/"
#CureatrPlayURL="https://messenger.play.cureatr.com/"

#APP TITLE
verifyTitle="Cureatr Messenger"

#***Institution screen***
cureatrlogo="//android.widget.ImageView[@resource-id='com.cureatr.messenger.dev:id/startup_logo']"
institution_label="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/institutions_instruction_label']"
searchinstitution="//android.widget.EditText[@resource-id='com.cureatr.messenger.dev:id/institutions_search_field']"
need_assistance_btn="//android.widget.Button[@resource-id='com.cureatr.messenger.dev:id/institutions_assistance_button']"
selectedinstitution="//android.widget.CheckedTextView[@resource-id='android:id/text1']"
institutiontoast="//android.widget.Button[@resource-id='com.cureatr.messenger.dev:id/missing_institution_button']"

#***Institution screen>>signin screen***
sign_in_screen="//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]"
Signinbackbutton="//android.widget.ImageButton[@resource-id='com.cureatr.messenger.dev:id/startup_back_button']"
institutioninsigninscreen="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/account_sign_in_notice_label']"
emailid="//android.widget.EditText[@resource-id='com.cureatr.messenger.dev:id/sign_in_email_field']"
password="//android.widget.EditText[@resource-id='com.cureatr.messenger.dev:id/sign_in_password_field']"
signinbutton="//android.widget.LinearLayout[1]/android.widget.Button[1]"
Forgotpasswordlink="//android.widget.Button[@resource-id='com.cureatr.messenger.dev:id/account_forgot_password_button']"
ortext="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/divider_view']"
createnewaccountlink="//android.widget.Button[@resource-id='com.cureatr.messenger.dev:id/account_toggle_button']"
#app_tour screen
tourscreen1="//android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]"
tourscreenimage1="//android.widget.RelativeLayout[1]/android.widget.ImageView[1]"
pageindicator1="//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]"
hippa_warning_text="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/app_pin_hipaa_warning']"
passcode_title="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/app_pin_title_label']"
skipbutton="//android.widget.Button[@text='Skip this']"
highlighted_pageindicator_page1="//android.widget.LinearLayout[1]/android.view.View[1]"
highlighted_pageindicator_page2="//android.widget.LinearLayout[1]/android.view.View[2]"
highlighted_pageindicator_page3="//android.widget.LinearLayout[1]/android.view.View[3]"
donebutton="//android.widget.Button[@text='Done']"

#***Institution screen>>signin screen>>dashboard screen***
compose_icon="//*[@resource-id='com.cureatr.messenger.dev:id/compose_thread_fab']"
notificationsicon="//android.widget.ImageView[@resource-id='com.cureatr.messenger.dev:id/menu_event_image']"
contactsicon="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/menu_search']"
settingsicon="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/menu_settings']"
listofmessages="//android.view.ViewGroup[@resource-id='com.cureatr.messenger.dev:id/swipe_layout']"
replymsgtext_1="//android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
#replymsgtext_n="//android.widget.FrameLayout[n]/android.widget.RelativeLayout[1]"
contactname="//android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.relativeLayout[1]/android.widget.TextView[1]"
threadsubject="//android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
#latestmsg="//android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.TextView[1]"
#latestcontactimage="//android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]"
latestunreadmsgscount="//android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
#latestunreadmsg

#***Institution screen>>signin screen>>dashboard screen***
listofmsgs="//android.widget.FrameLayout[@resource-id='com.cureatr.messenger.dev:id/fragment_container']"
latestmsg="//android.support.v7.widget.RecyclerView[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]"
existing_msg="//android.support.v7.widget.RecyclerView[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]"
latestcontactname="//android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
latestcontactimage="//android.support.v7.widget.RecyclerView[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]"
latestsubjectmsg="//android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView[1]"
latestmsgdate="//android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[2]"
workflowiconindashboard="//android.support.v7.widget.RecyclerView[1]/android.widget.FrameLayout[3]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]"
userstatusbutton="//android.widget.Button[@resource-id='com.cureatr.messenger.dev:id/user_status_button']"
urgent_tag="//android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]"

#***Institution screen>>signin screen>>dashboard screen>>click_on_message_with_workflow***
patient_info_icon="//android.support.v7.widget.LinearLayoutCompat[1]/android.widget.TextView[1]"
messages_tab_text="//android.support.v7.app.ActionBar.Tab[1]/android.widget.TextView[1]"
workflow_tab_text="//android.support.v7.app.ActionBar.Tab[2]/android.widget.TextView[1]"
Conversation_text="//android.widget.FrameLayout[1]/android.widget.TextView[1]"
msg_content="//android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]"
sendmsg="//android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
reply_msg="//android.widget.RelativeLayout[2]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
conv_start_time="//android.widget.FrameLayout[2]/android.widget.TextView[1]"
leave_thread_msg="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/leaveThreadMessage']"
patient_name="//android.widget.RelativeLayout[2]/android.widget.TextView[1]"
workflow_progress_text_1="//android.widget.RelativeLayout[2]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]"
#workflow_progress_text_n="//android.widget.RelativeLayout[n+1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]"
sent_time="//android.widget.RelativeLayout[4]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
readby_count_text="//android.widget.RelativeLayout[4]/android.widget.LinearLayout[1]/android.widget.TextView[2]"
unread_text="//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[2]"
conv_about_patient_text="//android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
view_patient_btn="//android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]"
enter_msg="//android.widget.EditText[1]"
urgent_icon="//android.widget.CheckBox[1]"
camera_option="//android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
gallery_option="//android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[2]"
permission_allow_button="//android.widget.Button[@resource-id='com.android.packageinstaller:id/permission_allow_button']"
image_n="//android.widget.FrameLayout[5]/android.widget.ImageView[1]"
image_1="//android.widget.FrameLayout[1]/android.widget.ImageView[1]"
images_list="//android.widget.GridView[@resource-id='com.android.documentsui:id/grid']"
recent_image_date="//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
recent_image="//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]"
audio_option="//android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[3]"
files_option="//android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[4]"

#***Institution screen>>signin screen>>dashboard screen>>click_on_message_with_workflow>>patient_info_icon***
patient_info_view_patient_btn="//*[@resource-id='com.cureatr.messenger.dev:id/menuPatientView']"
patient_info_settings_btn="//*[@resource-id='com.cureatr.messenger.dev:id/menuSettingsView']"

#***Institution screen>>signin screen>>dashboard screen>>click_on_message_with_workflow>>patient_info_icon>>patient_info_settings_screen***
#coversations_header_text="//android.view.ViewGroup[1]/android.widget.TextView[1]"
recipient_count="//*[@resource-id='com.cureatr.messenger.dev:id/threadMenuRecipientCount']"
profile_icon="//android.widget.LinearLayout[1]/android.widget.ImageView[1]"
add_delete_icon="//android.widget.LinearLayout[2]/android.widget.ImageView[1]"
profile_name_text="//android.view.ViewGroup[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
add_delete_text="//android.view.ViewGroup[1]/android.widget.LinearLayout[2]/android.widget.TextView[1]"
sound_notifications_text="//*[@resource-id='com.cureatr.messenger.dev:id/threadMenuMuteLabel']"
sound_notifications_checkbox="//*[@resource-id='com.cureatr.messenger.dev:id/threadMenuSoundCheckBox']"
archive_conv_btn="//*[@resource-id='com.cureatr.messenger.dev:id/threadMenuArchiveButton']"
leave_conv_btn="//*[@resource-id='com.cureatr.messenger.dev:id/threadMenuLeaveButton']"
#same xpath***Institution screen>>signin screen>>dashboard screen>>settings screen>>confirm popup***(popupheader,NObutton,YESbutton,alert_content)

#***Institution screen>>signin screen>>dashboard screen>>click_on_message_with_workflow>>patient_info_icon>>patient_info_settings_screen>>edit recipents screen***
#same xpath for #***Institution screen>>signin screen>>dashboard screen>>>compose screen***(cureatr_screen_header)

#***Institution screen>>signin screen>>dashboard screen>>click_on_message_with_workflow>>patient_info_icon>>patient_info_settings_screen>>add_delete screen***
#same xpath ***Institution screen>>signin screen>>dashboard screen>>click_on_message_with_workflow>>patient_info_icon>>patient_info_settings_screen***(cureatr_screen_header)
prof_img="//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]"
prof_name="//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
send_msg_link="//*[@resource-id='com.cureatr.messenger.dev:id/profile_message_container']"
#same xpath for#***Institution screen>>signin screen>>dashboard screen>>userstatus screen>>viewprofile screen***
#profileinstitution="//*[@resource-id='com.cureatr.messenger.dev:id/profile_institution']"
#profilespeciality="//*[@resource-id='com.cureatr.messenger.dev:id/profile_specialty']"
#profiletitle="//*[@resource-id='com.cureatr.messenger.dev:id/profile_title']"
current_services_header="//*[@resource-id='com.cureatr.messenger.dev:id/profile_roles_header']"
prof_service_1="//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]"
#prof_service_n="//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[n]"
doctor_conv_label="//*[@resource-id='com.cureatr.messenger.dev:id/profile_threads_header']"
#same xpath for #***Institution screen>>signin screen>>dashboard screen***(replymsgtext)
prof_view_all_conv="//*[@resource-id='com.cureatr.messenger.dev:id/profile_threads_footer']"
prof_patients_header="//*[@resource-id='com.cureatr.messenger.dev:id/profile_patients_header']"
prof_patient_1="//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
#prof_patient_n="//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.LinearLayout[n]/android.widget.TextView[1]"

#***Institution screen>>signin screen>>dashboard screen>>click_on_message_with_workflow>>patient_info_icon>>patient_info_settings_screen>>add_delete screen>>click on send_msg_link
#same xpath for #***Institution screen>>signin screen>>dashboard screen>>>compose screen***
#same xpath for #***Institution screen>>signin screen>>dashboard screen>>settings screen>>confirm popup***(popupheader,NObutton,YESbutton,alert_content)
#same xpath for #***Institution screen>>signin screen>>dashboard screen>>contacts screen***(contact_1,contactimage,contactname,specialityname,servicename)
#same xpath for ***Institution screen>>signin screen>>dashboard screen>>contacts screen>>patients screen>>recentpatientname screen(careteam_sendmsg_button)

#***Institution screen>>signin screen>>dashboard screen>>userstatus screen***
updatestatusheader="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/user_status_title']"
statusclosebutton="//*[@resource-id='com.cureatr.messenger.dev:id/user_status_close']"
userprofilename="//*[@resource-id='com.cureatr.messenger.dev:id/user_status_profile_name']"
profileimage="//*[@resource-id='com.cureatr.messenger.dev:id/user_status_profile_image']"
viewprofiletext="//*[@resource-id='com.cureatr.messenger.dev:id/user_status_view_profile']"
editprofiletext="//*[@resource-id='com.cureatr.messenger.dev:id/user_status_edit_profile']"
availableicon="//*[@resource-id='com.cureatr.messenger.dev:id/user_status_available_radio']"
busyicon="//*[@resource-id='com.cureatr.messenger.dev:id/user_status_busy_radio']"
offdutyicon="//*[@resource-id='com.cureatr.messenger.dev:id/user_status_off_radio']"
statusmessage="//*[@resource-id='com.cureatr.messenger.dev:id/user_status_editor']"
servicemessage="//*[@resource-id='com.cureatr.messenger.dev:id/user_status_select_service']"
coveragelayout="//*[@resource-id='com.cureatr.messenger.dev:id/user_status_covering_layout']"

#***Institution screen>>signin screen>>dashboard screen>>userstatus screen>>viewprofile screen***
editbutton="//*[@resource-id='com.cureatr.messenger.dev:id/menu_edit_profile']"
userimage="//android.widget.ImageView[1]"
profilename="//*[@resource-id='com.cureatr.messenger.dev:id/profile_name']"
helptext="//android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
profileinstitution="//*[@resource-id='com.cureatr.messenger.dev:id/profile_institution']"
profilespeciality="//*[@resource-id='com.cureatr.messenger.dev:id/profile_specialty']"
profiletitle="//*[@resource-id='com.cureatr.messenger.dev:id/profile_title']"

#***Institution screen>>signin screen>>dashboard screen>>userstatus screen>>editprofile screen***
#same xpath #***Institution screen>>signin screen>>dashboard screen>>userstatus screen>>viewprofile screen***(userimage)
listineditprofile="//android.widget.ScrollView[1]/android.widget.LinearLayout[1]"
editprofilename="//*[@resource-id='com.cureatr.messenger.dev:id/profile_edit_name']"
updateprofilephototext="//android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView[1]"
editspeciality="//*[@resource-id='com.cureatr.messenger.dev:id/profile_edit_specialty_container']"
edittitle="//*[@resource-id='com.cureatr.messenger.dev:id/profile_edit_title_container']"
emailtext="//android.widget.LinearLayout[4]/android.widget.TextView[1]"
editemail="//*[@resource-id='com.cureatr.messenger.dev:id/profile_edit_email']"
institutiontext="//android.widget.LinearLayout[4]/android.widget.TextView[3]"
editinstitution="//*[@resource-id='com.cureatr.messenger.dev:id/profile_edit_institution']"
editcontactsupport="//*[@resource-id='com.cureatr.messenger.dev:id/profile_edit_contact_support']"
donetext="//*[@resource-id='com.cureatr.messenger.dev:id/menu_edit_profile']"

#***Institution screen>>signin screen>>dashboard screen>>userstatus screen>>service screen***
search_all_services_text="//*[@resource-id='com.cureatr.messenger.dev:id/searchText']"
search_close_button="//*[@resource-id='com.cureatr.messenger.dev:id/xButton']"
clear_all_text="//*[@resource-id='com.cureatr.messenger.dev:id/clearAll']"
service_1="//android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[1]"
service_2="//android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[2]"
service_3="//android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[3]"
service_4="//android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[4]"
#xpath for nth service(service_n="//android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[n]") 
service_1_tickmark="//android.widget.RelativeLayout[1]/android.widget.ImageView[1]"
#xpath for nth service_tickmark (service_n_tickmark="//android.widget.RelativeLayout[n]/android.widget.ImageView[1]")

#***Institution screen>>signin screen>>dashboard screen>>userstatus screen>>editprofile screen>>updateprofilephoto screen***
picksavedphototext="//android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
tekenewphototext="//android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"

#***Institution screen>>signin screen>>dashboard screen>>events screen***
eventsheader="//android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.TextView[1]"
noeventstext="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/emptyTitle']"
anyeventstext="//android.widget.RelativeLayout[1]/android.widget.TextView[2]"

#***Institution screen>>signin screen>>dashboard screen>>contacts screen***
searchtext="//android.widget.EditText[@resource-id='com.cureatr.messenger.dev:id/searchMenuText']"
contactsbutton="//android.support.v7.app.ActionBar.Tab[1]/android.widget.TextView[1]"
patientsbutton="//android.support.v7.app.ActionBar.Tab[2]/android.widget.TextView[1]"
recentcontactsheader="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/directory_search_label']"
contact_1="//android.widget.ListView[1]/android.widget.RelativeLayout[1]"
#contact_n="//android.widget.ListView[1]/android.widget.RelativeLayout[n]"(for nth contact)
contactimage="//android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]"
contactname="//android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
specialityname="//android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
servicename="//android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.TextView[2]"
composeicon="//android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]"
#contact_info_icon="//android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]"

#***Institution screen>>signin screen>>dashboard screen>>contacts screen>>composeicon(new message screen)***
alert_content="//android.widget.TextView[@resource-id='android:id/message']"
#same xpaths for CANCEL and OK buttons--NObutton and YESbutton(#***Institution screen>>signin screen>>dashboard screen>>settings screen>>confirm popup***)
#same xpaths-(#***Institution screen>>signin screen>>dashboard screen>>>compose screen***)

#***Institution screen>>signin screen>>dashboard screen>>contacts screen>>patients screen***
recentpatientsheader="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/patient_search_label']"
recentpatientname="//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
genderandage="//android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"

#***Institution screen>>signin screen>>dashboard screen>>contacts screen>>patients screen>>recentpatientname screen
care_team_tab="//android.support.v7.app.ActionBar.Tab[1]/android.widget.TextView[1]"
history_tab="//android.support.v7.app.ActionBar.Tab[2]/android.widget.TextView[1]"
patient_info_tab="//android.support.v7.app.ActionBar.Tab[3]/android.widget.TextView[1]"
conv_help_text="//*[@resource-id='com.cureatr.messenger.dev:id/headerTitle']"
#selectioncircle="//android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]"
#same xpaths for Institution screen>>signin screen>>dashboard screen>>contacts screen(contactname,specialityname,servicename,composeicon,contactimage and selectioncircle)
patient_info_icon="//android.widget.RelativeLayout[1]/android.widget.ImageView[3]"
careteam_cancelbutton="//*[@resource-id='com.cureatr.messenger.dev:id/cancelButton']"
careteam_sendmsg_button="//*[@resource-id='com.cureatr.messenger.dev:id/sendMessageButton']"
#same xpaths for (#***Institution screen>>signin screen>>dashboard screen>>>compose screen***)

#***Institution screen>>signin screen>>dashboard screen>>contacts screen>>patients screen>>recentpatientname screen>>history_tab screen
#same xpaths for #***Institution screen>>signin screen>>dashboard screen>>contacts screen>>patients screen>>recentpatientname screen(conv_help_text)
history_conv_1="//android.widget.ListView[1]/android.widget.FrameLayout[2]"
#history_conv_n="//android.widget.ListView[1]/android.widget.FrameLayout[n+1]"
view_all_conv_btn="//android.widget.ListView[1]/android.widget.RelativeLayout[1]"
all_conv_1_msg="//android.support.v7.widget.RecyclerView[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]"
#all_conv_nth_msg="//android.support.v7.widget.RecyclerView[1]/android.widget.FrameLayout[n]/android.widget.RelativeLayout[1]"

#***Institution screen>>signin screen>>dashboard screen>>contacts screen>>patients screen>>recentpatientname screen>>patient_info_tab***
patient_info_screen_header="//android.widget.ListView[1]/android.widget.RelativeLayout[1]"
atient_info_screen_header_text="//android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
patient_info_screen_header_value="//android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]"
id_label="//android.widget.TextView[@text='ID Number']"
name_label="//android.widget.TextView[@text='Name']"
patient_dob_label="//android.widget.TextView[@text='DOB']"
sex_label="//android.widget.TextView[@text='Sex']"
location_label="//android.widget.TextView[@text='Location']"
#poc_rm_bed_label="//android.widget.TextView[@text='PoC · Rm · Bed']"
recent_diagnoses_label="//android.widget.TextView[@text='Recent Diagnoses']"
attending_physicians_label="//android.widget.TextView[@text='Attending Physician(s)']"
id_value="//android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
name_value="//android.widget.RelativeLayout[3]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
dob_value="//android.widget.RelativeLayout[4]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
sex_value="//android.widget.RelativeLayout[5]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
location_value="//android.widget.RelativeLayout[6]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
poc_rm_bed_value="//android.widget.RelativeLayout[7]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
recent_diagnoses_date="//android.widget.RelativeLayout[8]/android.widget.RelativeLayout[1]"
recent_diagnoses_text="//android.widget.RelativeLayout[9]/android.widget.RelativeLayout[1]"
attending_physician_date="//android.widget.RelativeLayout[10]/android.widget.RelativeLayout[1]"
attending_physician_text="//android.widget.RelativeLayout[11]/android.widget.RelativeLayout[1]"

#***Institution screen>>signin screen>>dashboard screen>>contacts screen>>patients screen>>composeicon(new message screen)***
listinnewmessage="//android.widget.ListView[@resource-id='com.cureatr.messenger.dev:id/dropdownListView']"
statusicon="//android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]"

#***Institution screen>>signin screen>>dashboard screen>>settings screen***
listcontent="//android.widget.FrameLayout[@resource-id='android:id/content']"
userdefaultimage="//android.widget.ImageView[@resource-id='com.cureatr.messenger.dev:id/prefIcon']"
userdetails="//android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[1]"
username="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/prefName']"
preferredinstitution="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/prefInstitution']"
preferredspeciality="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/prefSpecialty']"
preferredtitle="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/prefTitle']"
signoutbutton="//android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
nameindisablemode="//android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[2]"
manageaccountslink="//android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
recipientgroupslink="//android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
alertsoundlink="//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[5]"
urgentsoundlink="//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[6]"
mutepagertext="//android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
mutepagercheckbox="//android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.CheckBox[1]"
sortinboxtext="//android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
sortinboxcheckbox="//android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.CheckBox[1]"
showarchieveditemstext="//android.widget.LinearLayout[5]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
showarchievedcheckbox="//android.widget.LinearLayout[5]/android.widget.LinearLayout[1]/android.widget.CheckBox[1]"
securitysettingslink="//android.widget.LinearLayout[6]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
emailsupportlink="//android.widget.LinearLayout[7]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
resetpopuplink="//android.widget.LinearLayout[8]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
ratecureatrtext="//android.widget.LinearLayout[9]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
ratingicon="//android.widget.ImageView[@resource-id='android:id/icon']"
aboutcureatrlink="//android.widget.LinearLayout[10]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"

#***Institution screen>>signin screen>>dashboard screen>>settings screen>>confirm popup***
popupheader="//android.widget.TextView[@resource-id='android:id/alertTitle']"
yes_shareddevice_button="//android.widget.Button[@resource-id='android:id/button3']"
NObutton="//android.widget.Button[@resource-id='android:id/button2']"
YESbutton="//android.widget.Button[@resource-id='android:id/button1']"

#***Institution screen>>signin screen>>dashboard screen>>settings screen>>manageaccounts link***
addaccountlink="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/add_account']"
manageaccountstext="//android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
profileimage="//android.widget.ImageView[@resource-id='com.cureatr.messenger.dev:id/profile_image']"
profilename="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/name']"
profileemailid="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/email']"

#***Institution screen>>signin screen>>dashboard screen>>settings screen>>recipientgroups 
group_name_label="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/group_edit_name_label']"
group_name_input="//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]"
group_add_symbol="//android.widget.LinearLayout[2]/android.view.ViewGroup[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]"
addbutton="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/menu_add']"
nogroupstext="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/emptyTitle']"
creategroupstext="//android.widget.RelativeLayout[1]/android.widget.TextView[2]"
recipient_group_save_btn="//android.view.ViewGroup[1]/android.support.v7.widget.LinearLayoutCompat[1]/android.widget.TextView[1]"
recipient_profile="//android.view.ViewGroup[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]"
add_delete_recipient="//android.widget.LinearLayout[2]/android.view.ViewGroup[1]/android.widget.LinearLayout[2]/android.widget.ImageView[1]"
#***Institution screen>>signin screen>>dashboard screen>>settings screen>>alertsound screen***
#alertsoundtext="//android.widget.TextView[@resource-id='android:id/alertTitle']"(popupheader)
listinalert="//android.widget.FrameLayout[@resource-id='android:id/contentPanel']"
list1="//android.widget.ListView[1]/android.widget.CheckedTextView[1]"
listn="//android.widget.ListView[1]/android.widget.CheckedTextView[n]"
#same xpaths for urgentsound screen
#same xpaths for CANCEL and OK buttons--NObutton and YESbutton(#***Institution screen>>signin screen>>dashboard screen>>settings screen>>confirm popup***)

#***Institution screen>>signin screen>>dashboard screen>>settings screen>>securitysettings screen***
securitylist="//android.support.v7.widget.RecyclerView[@resource-id='com.cureatr.messenger.dev:id/list']"
changepasswordtext="//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[1]"
changeapppasscodetext="//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[2]"
automaticlock="//android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[3]"

#***Institution screen>>signin screen>>dashboard screen>>settings screen>>securitysettings screen>>changepassword screen***
password_hint="//*[@resource-id='com.cureatr.messenger.dev:id/password_requirements_label']"
current_password="//*[@resource-id='com.cureatr.messenger.dev:id/current_password']"
new_password="//*[@resource-id='com.cureatr.messenger.dev:id/new_password']"
change_password_button="//*[@resource-id='com.cureatr.messenger.dev:id/password_change_button']"
set_new_password_button="//*[@resource-id='com.cureatr.messenger.dev:id/password_set_button']"
change_pwd_hint_header="//*[@resource-id='com.cureatr.messenger.dev:id/password_change_title']"

#***Institution screen>>signin screen>>dashboard screen>>settings screen>>securitysettings screen>>changeapppasscode screen***
Forgot_passcode_btn="//*[@resource-id='com.cureatr.messenger.dev:id/app_pin_text_button']"
current_passcode_text="//*[@resource-id='com.cureatr.messenger.dev:id/app_pin_title_label']"
passcode_digit_1="//android.widget.LinearLayout[1]/android.widget.EditText[1]"
passcode_digit_2="//android.widget.LinearLayout[1]/android.widget.EditText[2]"
passcode_digit_3="//android.widget.LinearLayout[1]/android.widget.EditText[3]"
passcode_digit_4="//android.widget.LinearLayout[1]/android.widget.EditText[4]"
#same xpaths for new_passcode and confirm new_passcode flow

#***Institution screen>>signin screen>>dashboard screen>>settings screen>>securitysettings screen>>changeapppasscode screen>>Forgot_passcode_btn screen
#same xpath for #***Institution screen>>signin screen>>dashboard screen>>settings screen>>alertsound screen***(alertsoundtext)
#same xpath for #***Institution screen>>signin screen>>dashboard screen>>contacts screen>>composeicon(new message screen)(alert_content)
#same xpaths for CANCEL and OK buttons--NObutton and YESbutton(#***Institution screen>>signin screen>>dashboard screen>>settings screen>>confirm popup***)

#***Institution screen>>signin screen>>dashboard screen>>settings screen>>automaticlock popup***
#same xpath for #***Institution screen>>signin screen>>dashboard screen>>contacts screen>>composeicon(new message screen)(alert_content)
lock_immediate="//android.widget.CheckedTextView[1]"
lock_1min="//android.widget.CheckedTextView[2]"
lock_2min="//android.widget.CheckedTextView[3]"
lock_5min="//android.widget.CheckedTextView[4]"
lock_10min="//android.widget.CheckedTextView[5]"
lock_15min="//android.widget.CheckedTextView[6]"
#same xpaths for CANCEL and OK buttons--NObutton and YESbutton(#***Institution screen>>signin screen>>dashboard screen>>settings screen>>confirm popup***)

#***Institution screen>>signin screen>>dashboard screen>>settings screen>>emailsupport screen***
#same xpath for security list,CANCEL and NEW MESSAGE buttons--NObutton and YESbutton(#***Institution screen>>signin screen>>dashboard screen>>settings screen>>confirm popup***)

#***Institution screen>>signin screen>>dashboard screen>>settings screen>>aboutcureatr screen***
appversiontext="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/app_version_text']"
aboutcureatrtext="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/app_info_text']"
copyrighttext="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/app_copyright_text']"
legalnoticebutton="//android.widget.Button[@resource-id='com.cureatr.messenger.dev:id/legal_notices_button']"

#***Institution screen>>signin screen>>dashboard screen>>settings screen>>aboutcureatr screen>>legalnotice screen***
legalnoticetext="//android.view.ViewGroup[1]/android.widget.FrameLayout[2]"

#***Institution screen>>signin screen>>dashboard screen>>>compose screen***
backbuttonincompose="//android.widget.ImageButton[1]"
cureatr_screen_header="//android.view.ViewGroup[1]/android.widget.TextView[1]"
Tolabel="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/newThreadRecipientsLabel']"
Tofield="//android.widget.MultiAutoCompleteTextView[@resource-id='com.cureatr.messenger.dev:id/newThreadRecipientsInput']"
View_profile_link="//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.TextView[1]"
remove_conv_link="//android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.TextView[2]"
Tofieldcloseicon="//android.widget.Button[@resource-id='com.cureatr.messenger.dev:id/newThreadDirectoryButton']"
patientlabel="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/newThreadPatientLabel']"
patientfield="//android.widget.MultiAutoCompleteTextView[@resource-id='com.cureatr.messenger.dev:id/newThreadPatientCompletionView']"
workflowlabel="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/newThreadWorkflowLabel']"
subjectlabel="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/newThreadSubjectLabel']"
subjectfield="//android.widget.EditText[@resource-id='com.cureatr.messenger.dev:id/newThreadSubjectInput']"
msgtextbox="//android.widget.EditText[@resource-id='com.cureatr.messenger.dev:id/composerMessageEditText']"
urgenticon="//android.widget.CheckBox[@resource-id='com.cureatr.messenger.dev:id/composerUrgentCheckBox']"
camerabutton="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/composerCameraButton']"
gallerybutton="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/composerGalleryButton']"
audiobutton="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/composerAudioButton']"
fileattachmentbutton="//android.widget.TextView[@resource-id='com.cureatr.messenger.dev:id/composerFilesButton']"
quickmsgbutton="//android.widget.ImageView[@resource-id='com.cureatr.messenger.dev:id/quickMessageButton']"
send_btn_text="//*[@resource-id='com.cureatr.messenger.dev:id/sendOrQMWrap']"
send_text="//*[@resource-id='com.cureatr.messenger.dev:id/sendText']"
send_icon="//*[@resource-id='com.cureatr.messenger.dev:id/sendIcon']"
#camera_option="//android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
#gallery_option="//android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[2]"
#audio_option="//android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[3]"
#files_option="//android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[4]"
#quick_msg_icon="//android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]"

#***Institution screen>>signin screen>>dashboard screen>>>compose screen>>quickmsgbutton***

#quick_msg_listn="//android.widget.LinearLayout[n]/android.widget.LinearLayout[1]"
tap_to_send_text="//android.widget.LinearLayout[10]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
quickmsglist_cancel_button="//*[@resource-id='com.cureatr.messenger.dev:id/macros_cancel']"
edit_list_button="//*[@resource-id='com.cureatr.messenger.dev:id/macros_edit_macro_button']"
quick_msg_list1="//android.widget.LinearLayout[1]/android.widget.LinearLayout[1]"

#***Institution screen>>signin screen>>dashboard screen>>>compose screen>>quickmsgbutton>>edit_list_button screen***
#createmsgtextbox="//*[@resource-id='com.cureatr.messenger.dev:id/macros_new_edit_text']"
edit_quick_msg_done_btn="//android.widget.TextView[@text='Done']"
edit_quick_msg_save_btn="//android.widget.TextView[@text='Save']"
edit_add_btn="//*[@resource-id='com.cureatr.messenger.dev:id/macros_new_image_button']"
create_new_quick_msg="//*[@resource-id='com.cureatr.messenger.dev:id/macros_new_text_button']"
save_btn_created_msg="//*[@resource-id='com.cureatr.messenger.dev:id/save_button_edit']"

#delete_quick_msg_n="//android.widget.LinearLayout[n+1]/android.widget.ImageView[1]"(for nth quick msg deletion)
quick_msg_1_content="//android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
#quick_msg_n_content="//android.widget.LinearLayout[n+1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"(for nth quick msg content)
quick_msg_1_drag_btn="//android.widget.LinearLayout[2]/android.widget.ImageView[2]"
#quick_msg_n_drag_btn="//android.widget.LinearLayout[n+1]/android.widget.ImageView[2]"(for nth quick msg dragging)
edit_text_box="//android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.EditText[1]"

#***Institution screen>>signin screen>>dashboard screen>>>compose screen>>quickmsgbutton>>edit_list_button screen>>delete_quick_msg_1***
#***Institution screen>>signin screen>>dashboard screen>>settings screen>>confirm popup***(popupheader,NObutton,YESbutton,alert_content)

#***Institution screen>>signin screen>>dashboard screen>>>compose screen>>workflow screen***
selected_workflow="//android.widget.FrameLayout[1]/android.widget.TextView[1]"
other_workflows_header="//android.widget.FrameLayout[2]/android.widget.TextView[1]"
workflow_list="//*[@resource-id='com.cureatr.messenger.dev:id/workflowsListView']"
workflow_1="//android.widget.RelativeLayout[1]/android.widget.TextView[1]"
#workflow_n="//android.widget.RelativeLayout[n]/android.widget.TextView[1]"
preview_link_1="//android.widget.RelativeLayout[1]/android.widget.TextView[2]"
#preview_link_n="//android.widget.RelativeLayout[n]/android.widget.TextView[2]"
selected_workflow_tickmark="//*[@resource-id='com.cureatr.messenger.dev:id/checkedImg']"

#***Institution screen>>signin screen>>dashboard screen>>>compose screen>>workflow screen>>preview screen***(same for all workflows)
fields_list="//android.view.ViewGroup[1]/android.widget.FrameLayout[2]"
patient_name_label="//android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]"
DOB_label="//android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]"
gender_label="//android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]"
gender_m="//android.webkit.WebView[1]/android.view.View[1]/android.view.View[4]"
gender_f="//android.webkit.WebView[1]/android.view.View[1]/android.view.View[5]"
confirmation_label="//android.webkit.WebView[1]/android.view.View[1]/android.view.View[6]"
confirmation_checkbox="//android.webkit.WebView[1]/android.view.View[1]/android.view.View[7]"
postal_address_label="//android.webkit.WebView[1]/android.view.View[1]/android.view.View[8]"
use_this_workflow_btn="//android.widget.Button[@text='Use this workflow']"

quick_msg_list="//android.widget.LinearLayout[1]/android.widget.ListView[1]/*"
add_delete_icon_1="//android.widget.LinearLayout["
delete_quick_msg_2="]/android.widget.ImageView[1]"
quick_msgs_deletion=[quick_msg_list , add_delete_icon_1 , delete_quick_msg_2]


#TestXpath="]/android.widget.ImageView[1]"



#sravanitesting="//android.widget.LinearLayout[1]/android.widget.ListView[1]/*"
#genderggghh="//android.webkit.WebView[1]/android.view.View[1]/android.view.View[5]"
#TESt


