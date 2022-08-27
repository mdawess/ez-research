import { Mode } from "../types/types";

export const convertToArray = (object: any) => {
    const newArray = [];
    let data: keyof typeof object;
    for (data in object) {
      newArray.push({...object[data], title: data, saved: false, mode: "standard" as Mode})
    }
    return newArray
  }