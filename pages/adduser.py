from selenium import webdriver


class AddUser:

    view_admin = "menu_admin_viewAdminModule"
    add_btn_user = "btnAdd"
    user_role = "systemUser_userType"
    role = select(user_role)
    admin_user_role = role.select_by_value(1)
    ess_user_role = role.select_by_value(2)
    set_employeeName = "systemUser_employeeName_empName"
    set_userName = "systemUser_userName"
    set_status_of_user = "systemUser_status"
    status = select(set_status_of_user)
    enable_employee = status.select_by_index(1)
    disable_employee = status.select_by_index(2)
      set_emloyee_password= "systemUser_password"
    comfirm_employee_password = "systemUser_confirmPassword"
    save_employee_details = "btnSave"

    

