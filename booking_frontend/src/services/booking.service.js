import { BASE_URL, HEADERS } from "./constants";

export const createRoom = async (data) => {
  return fetch(`${BASE_URL}/rooms/`, {
    method: "POST",
    headers: HEADERS,
    body: JSON.stringify(data),
  });
};

export const updateRoom = async (id, data) => {
  return fetch(`${BASE_URL}/rooms/${id}`, {
    method: "PUT",
    headers: HEADERS,
    body: JSON.stringify(data),
  });
};

export const deleteRoom = async (id) => {
  return fetch(`${BASE_URL}/rooms/${id}`, {
    method: "DELETE",
  });
};

export const getFacilities = async () => {
  const res = await fetch(`${BASE_URL}/facility/`);
  return res.json();
};

export const getRooms = async () => {
  const res = await fetch(`${BASE_URL}/rooms/`);
  return res.json();
};

export const bookingService = {
  createRoom,
  updateRoom,
  deleteRoom,
  getFacilities,
  getRooms,
};
