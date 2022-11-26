import React from "react";
import CircularProgress from "@mui/material/CircularProgress";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardActionArea from "@mui/material/CardActionArea";
import Alert from "@mui/material/Alert";
import AlertTitle from "@mui/material/AlertTitle";
import { useQuery } from "react-query";
import { useNavigate, useParams } from "react-router-dom";

export default function Areas() {
  const { location_id, location_name } = useParams();
  const { isLoading, error, data } = useQuery(`get${location_id}Areas`, () =>
    fetch(`http://127.0.0.1:8000/areas/${location_id}/`).then((res) =>
      res.json()
    )
  );
  const navigate = useNavigate();

  if (isLoading) {
    return <CircularProgress />;
  }
  if (error) {
    return (
      <Alert severity="error">
        <AlertTitle>Error</AlertTitle>
        An error occurred while calling the API
      </Alert>
    );
  }
  return (
    <>
      <Typography variant="h3" mb={4} sx={{ textTransform: "capitalize" }}>
        {location_name} areas
      </Typography>
      <Grid container rowSpacing={2} columnSpacing={2}>
        {data.areas.map(({ name: name, poke_id: poke_id }) => (
          <Grid item key={poke_id}>
            <Card sx={{ height: "100%", width: 350 }}>
              <CardActionArea onClick={() => navigate(`${name}/${poke_id}`)}>
                <CardContent sx={{ marginLeft: "auto", marginRight: "auto" }}>
                  <Typography
                    variant="h5"
                    sx={{
                      height: 100,
                      textTransform: "capitalize",
                      textAlign: "center",
                    }}
                  >
                    {name}
                  </Typography>
                </CardContent>
              </CardActionArea>
            </Card>
          </Grid>
        ))}
      </Grid>
    </>
  );
}
