import { STORED_USER_KEY } from "./constants";
import { BASE_URL, HEADERS } from "./constants";

export const login = async (data) => {
  const res = await fetch(`${BASE_URL}/login/`, {
    method: "POST",
    headers: HEADERS,
    body: JSON.stringify({
      username: data.username,
      password: data.password,
    }),
  });

  const payload = await res.json();

  if (payload.current_user_id) {
    window.localStorage.setItem(STORED_USER_KEY, payload.current_user_id);
    return true;
  }

  return false;
};
