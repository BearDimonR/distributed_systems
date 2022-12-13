import React, { useState } from "react";
import Flippy, { FrontSide, BackSide } from "react-flippy";
import style from "./index.module.scss";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import { Typography } from "@mui/material";
import Tappable from "react-tappable/lib/Tappable";

const FlippyCard = ({ item }) => {
  const [isFlipped, setIsFlipped] = useState(false);
  return (
    <div className={style.flippyBackground}>
      <Tappable onTap={() => setIsFlipped(!isFlipped)}>
        <Flippy
          flipOnHover={false}
          flipDirection="horizontal"
          style={{ width: "100%", height: "100%", border: "none" }}
          isFlipped={isFlipped}
        >
          <FrontSide style={{ padding: "unset", borderRadius: "20px" }}>
            <Card className={style.card}>
              <CardMedia
                component="img"
                alt="green iguana"
                height="75%"
                src={item.pictureUrl}
                className={style.cardMedia}
              />
              <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                  {item.name}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  {item.type}
                </Typography>
              </CardContent>
            </Card>
          </FrontSide>
          <BackSide style={{ padding: "unset", borderRadius: "20px" }}>
            <Card className={style.card}>
              <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                  {item.name}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Brand: {item.brand}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Type: {item.type}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Percentages: {item.percentages}
                </Typography>
              </CardContent>
            </Card>
          </BackSide>
        </Flippy>
      </Tappable>
    </div>
  );
};

export default FlippyCard;
