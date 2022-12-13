import { toast } from "react-toastify";

export const handleError = async (action, msg) => {
  try {
    await action();
  } catch (err) {
    toast(
      `🤯 Oops! ${msg || "It looks like error occurred:"} ${err.message ?? err}`
    );
  }
};
