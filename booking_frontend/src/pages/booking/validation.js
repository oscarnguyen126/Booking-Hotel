import * as yup from "yup";

const yupObject = yup.object().shape({
  name: yup.string().required(),
  description: yup.string(),
  price: yup.number(),
  roomsize: yup.number(),
  facilities: yup
    .array()
    .of(
      yup.object().shape({
        name: yup.string(),
        checked: yup.boolean(),
      })
    )
    .compact((v) => !v.checked),
  image: yup.string(),
});

export const validate = (data) => {
  return yupObject.validate(data);
};
