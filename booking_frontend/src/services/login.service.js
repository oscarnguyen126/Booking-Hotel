import { STORED_USER_KEY } from "./constants";

export const login = async (data) => {
  const res = await fetch('/login')
  window.localStorage.setItem(STORED_USER_KEY, res.json().current_user_id)
};
export const logout = async () => {
  await fetch('/logout')
  window.localStorage.removeItem('user_id')
};
