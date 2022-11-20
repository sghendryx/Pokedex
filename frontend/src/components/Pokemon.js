import Card from "@mui/material/Card";
import CardMedia from "@mui/material/CardMedia";
import CardContent from "@mui/material/CardContent";
import Grid from "@mui/material/Grid";
import CircularProgress from "@mui/material/CircularProgress";
import Typography from "@mui/material/Typography";
import Alert from "@mui/material/Alert";
import AlertTitle from "@mui/material/AlertTitle";
import { useQuery } from "react-query";

export default function Pokemon() {
  const { isLoading, error, data } = useQuery("getPokemon", () =>
    fetch("http://127.0.0.1:8000/pokemon/").then((res) => res.json())
  );

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
    <Grid container rowSpacing={2} columnSpacing={2}>
      {data.pokemon.map((p) => (
        <Grid item xs={2} key={p.name}>
          <Card>
            <CardMedia
              component="img"
              style={{
                width: "auto",
              }}
              image={p.sprite}
            />
            <CardContent>
              <Typography
                variant="h5"
                style={{
                  "text-transform": "capitalize",
                }}
              >
                {p.name}
              </Typography>
            </CardContent>
          </Card>
        </Grid>
      ))}
    </Grid>
  );
}
